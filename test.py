import unittest
import random_graph_factory as rgf
from dijkstra import Dijkstra
from a_star import AStar
from bellmanford import BellmanFord
from floyd_warshall import FloydWarshall
import timeit


class Test(unittest.TestCase):
    def test(self):
        graph = rgf.generate_weighted_matrix_graph(20, 1, 10)
        a = timeit.default_timer()
        solution1 = Dijkstra.start(graph, graph[0], graph[-1])
        b = timeit.default_timer()
        print("dijkstra".ljust(12), b - a)
        a = timeit.default_timer()
        solution2 = AStar.start(graph, graph[0], graph[-1])
        b = timeit.default_timer()
        print("a*".ljust(12), b - a)
        a = timeit.default_timer()
        solution3 = BellmanFord.start(graph, graph[0], graph[-1])
        b = timeit.default_timer()
        print("bellmanford".ljust(12), b - a)
        self.assertEqual(solution1[0], solution2[0])
        self.assertEqual(solution1[0], solution3[0])
        self.assertEqual(solution2[0], solution3[0])

    def test_AStar_Equal_Dijkstra(self):
        graph = rgf.generate_weighted_matrix_graph(4, 1, 10)
        for i in range(1, len(graph)):
            solution1 = Dijkstra.start(graph, graph[0], graph[i])
            solution2 = AStar.start(graph, graph[0], graph[i])
            self.assertEqual(solution1[0], solution2[0])
        print("A* == Dijkstra")

    def test_BellmanFord_Equal_Dijkstra(self):
        graph = rgf.generate_weighted_matrix_graph(4, 1, 100)
        for i in range(1, len(graph)):
            solution1 = Dijkstra.start(graph, graph[0], graph[i])
            solution2 = BellmanFord.start(graph, graph[0], graph[i])
            self.assertEqual(solution1[0], solution2[0])
        print("BellmanFord == Dijkstra")

    def test_BellmanFord_Equal_FloydWarshall(self):
        graph = rgf.generate_weighted_graph(5, -1, 100)
        for i in range(1, len(graph)):
            solution1 = FloydWarshall.start(graph, graph[0], graph[i])
            solution2 = BellmanFord.start(graph, graph[0], graph[i])
            if solution1 or solution2:
                self.assertEqual(solution1[0], solution2[0])
        print("BellmanFord == FloydWarshall")

    def run(self, result=None):
        for i in range(100):
            self.test_AStar_Equal_Dijkstra()
        print("A* == Dijkstra 100 times")
        for i in range(100):
            self.test_BellmanFord_Equal_Dijkstra()
        print("BellmanFord == Dijkstra 100 times")
        for i in range(100):
            self.test_BellmanFord_Equal_FloydWarshall()
        print("BellmanFord == FloydWarshall 100 times")

