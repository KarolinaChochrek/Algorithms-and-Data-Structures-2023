#!/usr/bin/python
# -*- coding: utf-8 -*-

#skończone

class Macierz:

    def __init__(self, size, x=0):
        if isinstance(size, tuple):
            n, m = size
            self.macierz = [[x] * m for i in range(n)]
        else:
            self.macierz = size

    def __str__(self):
        for i in range(len(self.macierz)):
            for j in range(len(self.macierz[0])):
                print(self.macierz[i][j], end=" ")
            print()

    def __add__(self, other):
        if self.size()[0] == other.size()[0] and self.size()[1] == other.size()[1]:
            m, n = self.size()
            matrix = [[0] * n for i in range(m)]

            for i in range(self.size()[0]):
                for j in range(self.size()[1]):
                    matrix[i][j] = self.macierz[i][j] + other[i][j]

            res = Macierz(matrix)
            return res
        else:
            return None

    def __mul__(self, other):
        if self.size()[0] == other.size()[1] and self.size()[1] == other.size()[0]:
            m = self.size()[0]
            n = other.size()[1]
            matrix = [[0] * n for i in range(m)]

            for i in range(self.size()[0]):
                for j in range(other.size()[1]):
                    for k in range(other.size()[0]):
                        matrix[i][j] += self.macierz[i][k] * other[k][j]

            res = Macierz(matrix)
            return res
        else:
            return None

    def __getitem__(self, other):
        return self.macierz[other]

    def size(self):
        return len(self.macierz), len(self.macierz[0])

def transpose(macierz):
    m, n = macierz.size()
    matrix = [[0] * m for i in range(n)]
    for i in range(m):
        for j in range(n):
            matrix[j][i] = macierz[i][j]
    matrix_Transposed = Macierz(matrix)
    return matrix_Transposed


if __name__ == '__main__':
    m1 = Macierz(
        [[1, 0, 2],
         [-1, 3, 1]]
    )

    m2 = transpose(m1)
    m2.__str__()
    print()

    m3 = Macierz((2, 3), 1)

    m4 = m1 + m3
    m4.__str__()
    print()

    m5 = Macierz(
        [[3, 1],
         [2, 1],
         [1, 0]]
    )

    m6 = m1 * m5
    m6.__str__()


