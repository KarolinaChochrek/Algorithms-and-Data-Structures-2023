# skończone

# !/usr/bin/python
# -*- coding: utf-8 -*-

from typing import List, Dict

import polska


class Vertex:
    def __init__(self, data):
        self.x = data[0]
        self.y = data[1]
        self.key = data[2]

    def __hash__(self):
        return hash(self.key)

    def __eq__(self, other):
        if isinstance(other, Vertex):
            return self.key == other.key


class Edge:
    def __init__(self, vertex_1, vertex_2):
        self.vertex_1 = vertex_1
        self.vertex_2 = vertex_2


class AdjacencyMatrixGraph:
    def __init__(self):
        self.vertices = {}
        self.listOfVertices = []
        self.adjacency_matrix = []

    def isEmpty(self):
        return len(self.vertices) == 0

    def insertVertex(self, vertex: Vertex):
        if vertex not in self.vertices:
            self.listOfVertices.append(vertex)
            self.vertices[vertex] = len(self.listOfVertices) - 1
            for row in self.adjacency_matrix:
                row.append(0)
            self.adjacency_matrix.append([0] * len(self.vertices))

    def insertEdge(self, vertex1, vertex2, edge=1):
        if vertex1 not in self.vertices:
            self.insertVertex(vertex1)
        if vertex2 not in self.vertices:
            self.insertVertex(vertex2)
        index1 = self.getVertexIdx(vertex1)
        index2 = self.getVertexIdx(vertex2)
        self.adjacency_matrix[index1][index2] = edge
        self.adjacency_matrix[index2][index1] = edge

    def deleteVertex(self, vertex):
        if vertex in self.vertices:
            index = self.vertices[vertex]
            del self.vertices[vertex]
            self.listOfVertices.remove(vertex)
            self.adjacency_matrix.pop(index)
            for row in self.adjacency_matrix:
                row.pop(index)

    def deleteEdge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            index1 = self.getVertexIdx(vertex1)
            index2 = self.getVertexIdx(vertex2)
            self.adjacency_matrix[index1][index2] = 0

    def getVertexIdx(self, vertex):
        return self.vertices[vertex]

    def getVertex(self, index):
        for key, value in self.vertices.items():
            if value == index:
                return key

    def neighboursIdx(self, index):
        list_of_neighbours = []
        for i in self.adjacency_matrix[index]:
            if self.adjacency_matrix[index][i] == 1:
                list_of_neighbours.append(i)
            return list_of_neighbours

    def order(self):
        return len(self.vertices)

    def size(self):
        return sum([sum(row) for row in self.adjacency_matrix]) // 2

    def edges(self):
        edge_list = []
        for row in range(len(self.adjacency_matrix)):
            for col in range(len(self.adjacency_matrix[row])):
                if self.adjacency_matrix[row][col] == 1:
                    edge_list.append((self.getVertex(row).key, self.getVertex(col).key))
        print(edge_list)
        return edge_list


class AdjacencyListGraph:
    def __init__(self):
        self.vertices = {}
        self.listOfVertices: List[Vertex] = []
        self.adj_list: Dict[int, List[int]] = {}

    def isEmpty(self) -> bool:
        return len(self.listOfVertices) == 0

    def insertVertex(self, vertex: Vertex) -> None:
        if vertex not in self.listOfVertices:
            self.listOfVertices.append(vertex)
            self.vertices[vertex] = len(self.listOfVertices) - 1
            self.adj_list[self.getVertexIdx(vertex)] = []

    def insertEdge(self, vertex1: Vertex, vertex2: Vertex) -> None:
        if vertex1 not in self.listOfVertices:
            self.insertVertex(vertex1)
        if vertex2 not in self.listOfVertices:
            self.insertVertex(vertex2)
        vertex1_idx = self.getVertexIdx(vertex1)
        vertex2_idx = self.getVertexIdx(vertex2)
        self.adj_list[vertex1_idx].append(vertex2_idx)

    def deleteVertex(self, vertex: Vertex) -> None:
        if vertex not in self.listOfVertices:
            return
        vertex_idx = self.getVertexIdx(vertex)
        for key, value in self.adj_list.items():
            if vertex_idx in value:
                value.remove(vertex_idx)
        self.adj_list[vertex_idx] = []
        self.listOfVertices.pop(vertex_idx)

    def deleteEdge(self, v1: Vertex, v2: Vertex) -> None:
        if v1 in self.vertices and v2 in self.vertices:
            index1 = self.getVertexIdx(v1)
            index2 = self.getVertexIdx(v2)
            self.adj_list[index1].remove(index2)

    def getVertexIdx(self, vertex: Vertex) -> int:
        return self.vertices[vertex]

    def getVertex(self, vertex_idx: int) -> Vertex:
        return self.listOfVertices[vertex_idx]

    def neighboursIdx(self, vertex_idx: int) -> List[int]:
        return self.adj_list[vertex_idx]

    def order(self) -> int:
        return len(self.adj_list)

    def size(self) -> int:
        return sum([len(self.adj_list[vertex]) for vertex in self.adj_list]) // 2

    def edges(self) -> List[tuple]:
        edges = []
        for vertex_idx in self.adj_list:
            for neighbour_idx in self.adj_list[vertex_idx]:
                edges.append((self.listOfVertices[vertex_idx].key, self.listOfVertices[neighbour_idx].key))
        return edges


if __name__ == '__main__':
    poland1 = AdjacencyMatrixGraph()
    poland2 = AdjacencyListGraph()
    for vertex1, vertex2 in polska.graf:
        v1 = Vertex(polska.slownik[vertex1])
        v2 = Vertex(polska.slownik[vertex2])
        poland1.insertEdge(v1, v2)
        poland2.insertEdge(v1, v2)
    poland1.deleteEdge(Vertex(polska.slownik['W']), Vertex(polska.slownik['E']))
    poland1.deleteEdge(Vertex(polska.slownik['E']), Vertex(polska.slownik['W']))
    poland1.deleteVertex(Vertex(polska.slownik['K']))
    polska.draw_map(poland1.edges())
    poland2.deleteEdge(Vertex(polska.slownik['W']), Vertex(polska.slownik['E']))
    poland2.deleteEdge(Vertex(polska.slownik['E']), Vertex(polska.slownik['W']))
    poland2.deleteVertex(Vertex(polska.slownik['K']))
    polska.draw_map(poland2.edges())


