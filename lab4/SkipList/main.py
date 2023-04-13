#skończone

#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import random

class SkipListNode:
    def __init__(self, key, value, levels):
        self.key = key
        self.value = value
        self.levels = levels
        self.next = [None] * levels

    def __str__(self):
        return f"{self.key} : {self.value}"

class SkipList:
    def __init__(self, maxLevel):
        self.head = SkipListNode(None, None, maxLevel)
        self.maxLevel = maxLevel

    def randomLevel(self, p=0.5, maxLevel=None):
        lvl = 1
        while random() < p and lvl < (maxLevel or self.maxLevel):
            lvl += 1
        return lvl

    def search(self, key):
        node = self.head
        for lvl in range(self.maxLevel - 1, -1, -1):
            while node.next[lvl] and node.next[lvl].key < key:
                node = node.next[lvl]
        node = node.next[0]
        if node and node.key == key:
            return node.value
        else:
            return None

    def insert(self, key, value):
        prev = [None] * self.maxLevel
        node = self.head
        for lvl in range(self.maxLevel - 1, -1, -1):
            while node.next[lvl] and node.next[lvl].key < key:
                node = node.next[lvl]
            prev[lvl] = node
        node = node.next[0]
        if node and node.key == key:
            node.value = value
        else:
            newLevel = self.randomLevel()
            newNode = SkipListNode(key, value, newLevel)
            for lvl in range(newLevel):
                newNode.next[lvl] = prev[lvl].next[lvl]
                prev[lvl].next[lvl] = newNode

    def remove(self, key):
        prev = [None] * self.maxLevel
        node = self.head
        for lvl in range(self.maxLevel - 1, -1, -1):
            while node.next[lvl] and node.next[lvl].key < key:
                node = node.next[lvl]
            prev[lvl] = node
        node = node.next[0]
        if node and node.key == key:
            for lvl in range(self.maxLevel):
                if prev[lvl].next[lvl] != node:
                    break
                prev[lvl].next[lvl] = node.next[lvl]
                node.next[lvl] = None

    def displayList_(self):
        node = self.head.next[0]  # pierwszy element na poziomie 0
        keys = []                           # lista kluczy na tym poziomie
        while node != None:
            keys.append(node.key)
            node = node.next[0]

        for lvl in range(self.maxLevel-1, -1, -1):
            print("{}: ".format(lvl), end=" ")
            node = self.head.next[lvl]
            idx = 0
            while(node != None):
                while node.key>keys[idx]:
                    print("  ", end=" ")
                    idx+=1
                idx+=1
                print("{:2d}".format(node.key), end=" ")
                node = node.next[lvl]
            print("")


if __name__ == '__main__':
    height = 6
    skip_list = SkipList(height)
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"]
    for i in range(1, 16):
        skip_list.insert(i, letters[i - 1])
    skip_list.displayList_()
    print(skip_list.search(2))
    skip_list.insert(2, "Z")
    print(skip_list.search(2))
    skip_list.remove(5)
    skip_list.remove(6)
    skip_list.remove(7)
    skip_list.displayList_()
    skip_list.insert(6, "W")
    skip_list.displayList_()

    for i in range(15, 0, -1):
        skip_list.insert(i, letters[i - 1])
    skip_list.displayList_()
    print(skip_list.search(2))
    skip_list.insert(2, "Z")
    print(skip_list.search(2))
    skip_list.remove(5)
    skip_list.remove(6)
    skip_list.remove(7)
    skip_list.displayList_()
    skip_list.insert(6, "W")
    skip_list.displayList_()