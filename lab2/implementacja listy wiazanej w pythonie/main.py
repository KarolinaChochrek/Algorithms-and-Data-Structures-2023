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

    def __repr__(self):
        return f"('{self.university}', '{self.city}', {self.year})\n"

    def __str__(self):
        return f"('{self.university}', '{self.city}', {self.year})\n"


class LinkedList:

    def __init__(self):
        self.head = None

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
        self.head = None

    def add(self, node):
        node.next = self.head
        self.head = node

    def append(self, node) -> None:
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    def remove(self) -> None:
        if self.head is None:
            print("List is empty")

        self.head = self.head.next
        return

    def remove_end(self) -> None:
        if self.head is None:
            print("List is empty")

        previous_node = self.head
        for node in self:
            if node.next is None:
                previous_node.next = None
                return
            previous_node = node


    def is_empty(self) -> bool:
        if self.head is None:
            return True

    def length(self) -> int:
        i = 0
        node = self.head

        while node is not None:
            i += 1
            node = node.next
        print(i)

    def get(self) -> Node:
        if self.head is None:
            raise Exception("List is empty")

        print(self.head)


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

    uczelnie.length()

    uczelnie.remove()

    uczelnie.get()

    uczelnie.remove_end()

    print(uczelnie)

    uczelnie.destroy()

    print(uczelnie.is_empty())

    uczelnie.remove()

    uczelnie.remove_end()

