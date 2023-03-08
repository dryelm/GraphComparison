from queue import PriorityQueue
from random_graph_factory \
    import generate_weighted_graph, generate_weighted_matrix_graph
from node import Node
from edge import Edge


class AStar:
    @staticmethod
    def heuristic_func(node: Node, target: Node):
        return abs(target.name[0] - node.name[0]) + \
                abs(target.name[1] - node.name[1])

    @staticmethod
    def start(graph: list[Node], start: Node, target: Node):
        distances = {node: float("inf") for node in graph}
        distances[start] = 0
        to_visit = PriorityQueue()
        to_visit.put((0, [start]))
        while to_visit.qsize() != 0:
            path = to_visit.get()[1]
            if path[-1] == target:
                return distances[path[-1]], path
            for edge in path[-1].get_edges():
                next_node = edge.get_other_node(path[-1])
                if distances[path[-1]] + edge.get_cost()\
                        < distances[next_node]:
                    distances[next_node] = distances[path[-1]]\
                                           + edge.get_cost()
                    to_visit.put(
        (distances[next_node] + AStar.heuristic_func(next_node, target),
                        path + [next_node]))

    def __str__(self):
        return "A*"


if __name__ == "__main__":
    graph = generate_weighted_matrix_graph(100, 0, 100)
    print(AStar.start(graph, graph[0], graph[-1]))
    node1 = Node(0)
    node2 = Node(1)
    node3 = Node(2)
    edge1 = Edge(node1, node3, 5, True)
    node1.add_edge(edge1)
    edge2 = Edge(node1, node2, 1, True)
    node1.add_edge(edge2)
    edge3 = Edge(node2, node3, 1, True)
    node2.add_edge(edge3)
    print(
       [str(x) for x in AStar.start([node1, node2, node3], node1, node3)])