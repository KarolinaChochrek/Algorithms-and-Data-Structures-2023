#odesłana wersja

#skończone

#!/usr/bin/python
# -*- coding: utf-8 -*-

class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashTable:
    def __init__(self, size, c1=1, c2=0):
        self.size = size
        self.table = [None for _ in range(size)]
        self.c1 = c1
        self.c2 = c2
        self.num_entries = 0

    def hash_func(self, key):
        if isinstance(key, int):
            return key % self.size
        elif isinstance(key, str):
            return sum(ord(c) for c in key) % self.size
        else:
            raise TypeError("Invalid key type")

    def probe_func(self, idx, i):
        return (idx + self.c1 * i + self.c2 * i ** 2) % self.size

    def search(self, key):
        idx = self.hash_func(key)
        if isinstance(self.table[idx], Entry) and self.table[idx].key == key:
            return self.table[idx].value

        for i in range(1, len(self.table)):
            new_idx = self.probe_func(idx, i)
            if self.table[new_idx] is not None:
                if self.table[new_idx].key == key:
                    return self.table[new_idx].value

        if self.table[idx] is None:
            return None
        return None

    def insert(self, entry):
        idx: int = self.hash_func(entry.key)
        if self.table[idx] is None:
            self.table[idx] = entry
            return
        if isinstance(self.table[idx], Entry) and self.table[idx].key == entry.key:
            self.table[idx] = entry
            return
        for i in range(1, len(self.table)):
            new_idx = self.probe_func(idx, i)
            if isinstance(self.table[new_idx], Entry) and self.table[new_idx].key == entry.key:
                self.table[new_idx] = entry
                return
            if self.table[new_idx] is None:
                self.table[new_idx] = entry
                return
        print("Brak miejsca")

    def remove(self, key):
        idx = self.hash_func(key)
        i = 0
        while self.table[idx] is not None and i < self.size:
            if self.table[idx].key == key:
                self.table[idx] = None
                self.num_entries -= 1
                return
            i += 1
            idx = self.probe_func(idx, i)
        print("Brak danej")

    def __str__(self):
        entries = []
        for i in range(self.size):
            if self.table[i] is not None:
                entries.append(f"{self.table[i].key} : {self.table[i].value}")
            else:
                entries.append("None")
        return "{" + ", ".join(entries) + "}"

if __name__ == '__main__':
    def first_test(c1, c2):
        d = HashTable(13, c1, c2)
        l = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"]
        for i in range(1, 16):
            if i == 6:
                d.insert(Entry(18, "F"))
                continue
            if i == 7:
                d.insert(Entry(31, "G"))
                continue
            d.insert(Entry(i, l[i - 1]))

        print(d)
        print(d.search(5))
        print(d.search(14))
        d.insert(Entry(5, "Z"))
        print(d.search(5))
        d.remove(5)
        print(d)
        print(d.search(31))

        d.insert(Entry("W", "test"))
        print(d)


    def second_test(c1, c2):
        d = HashTable(13, c1, c2)
        l = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"]
        for i in range(1, 14):
            d.insert(Entry(13 * i, l[i - 1]))
        print(d)

    first_test(1, 0)
    second_test(1, 0)
    second_test(0, 1)
    first_test(0, 1)
