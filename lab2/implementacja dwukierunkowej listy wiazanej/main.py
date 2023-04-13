#skończone

#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Tuple

class Node:

    def __init__(self, data: Tuple[str, str, int]):
        self.university = data[0]
        self.city = data[1]
        self.year = data[2]
        self.next = None
        self.prev = None

    def __repr__(self):
        return f"-> ('{self.university}', '{self.city}', {self.year})\n"

    def __str__(self):
        return f"-> ('{self.university}', '{self.city}', {self.year})\n"


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __str__(self):
        element: str = ""
        for current_node in self:
            element += current_node.__str__()
        return element

    def destroy(self) -> None:
        self.head.next.prev = None
        self.head = None
        self.tail.prev.next = None
        self.tail = None

    def add(self, node):
        node.next = self.head
        if self.head != None:
            self.head.prev = node
            self.head = node
            node.prev = None
        else:
            self.head = node
            self.tail = node
            node.prev = None

    def append(self, node) -> None:
        node.prev = self.tail

        if self.tail is None:
            self.head = node
            self.tail = node
            node.next = None
        else:
            self.tail.next = node
            node.next = None
            self.tail = node

    def remove(self):
        if self.head is None:
            return
        else:
            temp = self.head
            if temp.next is None:
                self.tail = None
                self.head = None
            else:
                temp.next.prev = None
                self.head = temp.next
                temp.next = None


    def remove_end(self):
        if self.tail is None:
            return
        else:
            temp = self.tail
            if temp.prev is None:
                self.tail = None
                self.head = None
            else:
                temp.prev.next = None
                self.tail = temp.prev
                temp.prev = None


    def is_empty(self) -> bool:
        if self.head is None:
            return True

    def length(self) -> int:
        i = 0
        node = self.head

        while node is not None:
            i += 1
            node = node.next
        return i

    def get(self) -> Node:
        if self.head is None:
            raise Exception("List is empty")

        return self.head


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    nodes = [('AGH', 'Kraków', 1919),
    ('UJ', 'Kraków', 1364),
    ('PW', 'Warszawa', 1915),
    ('UW', 'Warszawa', 1915),
    ('UP', 'Poznań', 1919),
    ('PG', 'Gdańsk', 1945)]

    uczelnie = LinkedList()

    for i in range(3):
        uczelnie.append(Node(nodes[i]))

    for i in range(3, 6):
        uczelnie.add(Node(nodes[i]))

    print(uczelnie)

    print(uczelnie.length())

    uczelnie.remove()

    print(uczelnie.get())

    uczelnie.remove_end()

    print(uczelnie)

    uczelnie.destroy()

    print(uczelnie.is_empty())

    uczelnie.remove()

    uczelnie.append(Node(nodes[0]))

    uczelnie.remove_end()

    print(uczelnie)

