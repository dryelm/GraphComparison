import numpy as np
from node import Node
from edge import Edge


def generate_oriented_graph(size, expected_amount_of_edges: int):
    rand_matrix = np.random.randint(0, size, (size, size))
    for i in range(len(rand_matrix)):
        for j in range(len(rand_matrix[i])):
            if rand_matrix[i][j] < expected_amount_of_edges:
                rand_matrix[i][j] = 1
            else:
                rand_matrix[i][j] = 0

    nodes = [Node(i) for i in range(size)]
    for i in range(len(rand_matrix)):
        for j in range(len(rand_matrix[i])):
            if rand_matrix[i, j]:
                edge = Edge(nodes[i], nodes[j], 1, True)
                nodes[i].add_edge(edge)

    return nodes


def generate_weighted_graph(size, min_cost: int, max_cost: int):
    rand_matrix = np.random.randint(min_cost, max_cost+1, (size, size))
    nodes = [Node(i) for i in range(size)]
    for i in range(len(rand_matrix)):
        for j in range(len(rand_matrix[i])):
            if rand_matrix[i][j]:
                edge = Edge(nodes[i], nodes[j], rand_matrix[i][j], True)
                nodes[i].add_edge(edge)

    return nodes

# generates a random graph which is given by two coordinates. each vertex is associated only with vertices whose coordinates differ by one
def generate_weighted_matrix_graph(size, min_cost: int, max_cost: int):
    nodes = [Node((i, j)) for j in range(size) for i in range(size)]
    for i in range(size):
        for j in range(size):
            if i > 0:
                edge = Edge(nodes[i*size+j], nodes[(i-1)*size+j], np.random.randint(min_cost, max_cost+1), True)
                nodes[i*size+j].add_edge(edge)

            if i < size - 1:
                edge = Edge(nodes[i*size + j], nodes[(i+1)*size + j], np.random.randint(min_cost, max_cost+1), True)
                nodes[i*size + j].add_edge(edge)

            if j > 0:
                edge = Edge(nodes[i*size + j], nodes[i*size + j-1], np.random.randint(min_cost, max_cost+1), True)
                nodes[i*size + j].add_edge(edge)

            if j < size - 1:
                edge = Edge(nodes[i*size + j], nodes[i*size + j + 1], np.random.randint(min_cost, max_cost+1), True)
                nodes[i*size + j].add_edge(edge)
    return nodes
