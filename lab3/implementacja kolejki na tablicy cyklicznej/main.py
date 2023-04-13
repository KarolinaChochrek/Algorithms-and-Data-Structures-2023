#skończone

#!/usr/bin/python
# -*- coding: utf-8 -*-

class Queue:
    def __init__(self):
        self.tab = [None for i in range(5)]
        self.idx_dequeue = 0
        self.idx_enqueue = 0

    def is_empty(self) -> bool:
        return self.idx_dequeue == self.idx_enqueue

    def peek(self):
        if len(self.tab) == 0:
            return None

        return self.tab[self.idx_dequeue]

    def dequeue(self) -> int:
        element = self.tab[self.idx_dequeue]
        if element is None:
            return None
        self.tab[self.idx_dequeue] = None
        if self.idx_dequeue == len(self.tab) - 1:
            self.idx_dequeue = 0
        else:
            self.idx_dequeue += 1
        return element

    def enqueue(self, data) -> None:
        self.tab[self.idx_enqueue] = data
        if self.idx_enqueue == len(self.tab) - 1:
            self.idx_enqueue = 0
        else:
            self.idx_enqueue += 1
        if self.idx_enqueue == self.idx_dequeue:
            self.realloc(self.idx_enqueue)

    def realloc(self, idx) -> None:
        new_tab = [None for i in range(2 * len(self.tab))]
        new_tab[0:idx] = self.tab[0:idx]
        new_tab[-(len(self.tab) - idx):] = self.tab[idx:]
        self.idx_dequeue += len(self.tab)
        self.tab = new_tab
        return self.tab

    def __str__(self):
        return f"{self.tab}"

    def real_queue(self) -> str:
        queue = "["
        our_tab = self.tab
        our_idx = self.idx_dequeue
        while our_tab[our_idx] is not None:
            queue += str(our_tab[our_idx])
            queue += ", "
            if our_idx == len(our_tab) - 1:
                our_idx = 0
            else:
                our_idx += 1
        size = len(queue)
        new_queue = queue[:size - 2]
        new_queue += "]"

        if new_queue == "]":
            new_queue = '[]'

        return new_queue


if __name__ == '__main__':

    kolejka = Queue()

    for i in range(1, 5):
        kolejka.enqueue(i)

    print(kolejka.dequeue())
    print(kolejka.peek())
    print(kolejka.real_queue())

    for i in range(5, 9):
        kolejka.enqueue(i)

    print(kolejka)

    front = kolejka.dequeue()
    while front is not None:
        print(front)
        front = kolejka.dequeue()

    print(kolejka.real_queue())

