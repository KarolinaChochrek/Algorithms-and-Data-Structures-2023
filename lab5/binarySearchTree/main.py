# skończone

# !/usr/bin/python
# -*- coding: utf-8 -*-

class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def search(self, key):
        return self.__search(self.root, key)

    def __search(self, node, key):
        if node is None:
            return None
        if node.key == key:
            return node.data
        if key < node.key:
            return self.__search(node.left, key)
        else:
            return self.__search(node.right, key)

    def insert(self, key, data):
        if self.root is None:
            self.root = Node(key, data)
            return
        return self.__insert(self.root, key, data)

    def __insert(self, node, key, data):
        if key == node.key:
            node.data = data
            return
        elif key < node.key and node.left is None:
            node.left = Node(key, data)
            return
        elif key > node.key and node.right is None:
            node.right = Node(key, data)
            return
        elif key < node.key:
            return self.__insert(node.left, key, data)
        elif key > node.key:
            return self.__insert(node.right, key, data)

    def delete(self, key):
        if self.root is None:
            raise Exception("Tree does not exist!")
        return self.__delete(self.root, key)

    def __delete(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.left = self.__delete(node.left, key)
        elif key > node.key:
            node.right = self.__delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                successor = self.__get_successor(node.right)
                node.key = successor.key
                node.data = successor.data
                node.right = self.__delete(node.right, successor.key)
        return node

    def __get_successor(self, node):
        while node.left is not None:
            node = node.left
        return node

    def print_tree(self):
        print("==============")
        self.__print_tree(self.root, 0)
        print("==============")

    def __print_tree(self, node, lvl):
        if node is not None:
            self.__print_tree(node.right, lvl + 5)
            print()
            print(lvl * " ", node.key, node.data)
            self.__print_tree(node.left, lvl + 5)

    def print(self):
        return self.__print(self.root)

    def __print(self, node):
        if node.left:
            self.__print(node.left)
        print(f"{node.key} {node.data}", end=",")
        if node.right:
            self.__print(node.right)

    def height(self, start_key=None):
        if start_key is None:
            start_key = self.root.key
        if self.root.key != start_key:
            return self.__height(self.find_the_node(start_key, self.root))
        return self.__height(self.root)

    def __height(self, node):
        if node is None:
            return -1
        else:
            left_height = self.__height(node.left)
            right_height = self.__height(node.right)
            return 1 + max(left_height, right_height)

    def find_the_node(self, start_key, node):
        if node.key == start_key:
            return node
        if start_key < node.key:
            return self.find_the_node(start_key, node.left)
        if start_key > node.key:
            return self.find_the_node(start_key, node.right)


if __name__ == '__main__':
    bst = BST()

    bst.insert(50, 'A')
    bst.insert(15, 'B')
    bst.insert(62, 'C')
    bst.insert(5, 'D')
    bst.insert(20, 'E')
    bst.insert(58, 'F')
    bst.insert(91, 'G')
    bst.insert(3, 'H')
    bst.insert(8, 'I')
    bst.insert(37, 'J')
    bst.insert(60, 'K')
    bst.insert(24, 'L')

    bst.print_tree()
    bst.print()
    print()
    print(bst.search(24))
    bst.insert(20, 'AA')
    bst.insert(6, 'M')
    bst.delete(62)
    bst.insert(59, 'N')
    bst.insert(100, 'P')
    bst.delete(8)
    bst.delete(15)
    bst.insert(55, 'R')
    bst.delete(50)
    bst.delete(5)
    bst.delete(24)
    print(bst.height())
    bst.print()
    print()
    bst.print_tree()
