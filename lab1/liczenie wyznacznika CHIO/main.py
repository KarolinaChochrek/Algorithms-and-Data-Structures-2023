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

    def __setitem__(self, key, value):
        self.macierz[key] = value

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


def determinant_size_2x2(macierz: Macierz) -> float:
        return macierz[0][0] * macierz[1][1] - macierz[1][0] * macierz[0][1]


def determinant_chio(a: float, macierz: Macierz) -> float:

    if macierz.size() == (2, 2):
        return a * determinant_size_2x2(macierz)

    if macierz[0][0] == 0:
        for i in range(macierz.size()[0] + 1):
            if macierz[i][0] != 0:
                macierz[0], macierz[i] = macierz[i], macierz[0]

                a *= -1
                break

    wsp = a * 1 / (macierz[0][0] ** (macierz.size()[0] - 2))

    nowa_macierz = []
    for i in range(macierz.size()[0] - 1):
        new_n = []
        for j in range(macierz.size()[1] - 1):
            new_n.append(determinant_size_2x2(Macierz([[macierz[0][0], macierz[0][j + 1]],
                                                          [macierz[i + 1][0], macierz[i + 1][j + 1]]])))
        nowa_macierz.append(new_n)
    return determinant_chio(wsp, Macierz(nowa_macierz))


if __name__ == '__main__':
    m1 = Macierz(
        [
            [5, 1, 1, 2, 3],
            [4, 2, 1, 7, 3],
            [2, 1, 2, 4, 7],
            [9, 1, 0, 7, 0],
            [1, 4, 7, 2, 2]
        ]
    )

    m2 = Macierz(
        [
            [0, 1, 1, 2, 3],
            [4, 2, 1, 7, 3],
            [2, 1, 2, 4, 7],
            [9, 1, 0, 7, 0],
            [1, 4, 7, 2, 2]
        ]
    )

    print(determinant_chio(1.0, m1))

    print(determinant_chio(1.0, m2))
