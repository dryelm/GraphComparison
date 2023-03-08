from node import Node
from edge import Edge
from queue import LifoQueue
import random_graph_factory as rgf

class DFS:
    @staticmethod
    def start(graph: list[Node], start_node: Node, target: Node):
        visited = []
        to_visit = LifoQueue()
        to_visit.put([start_node])
        while to_visit.qsize() != 0:
            path = to_visit.get()
            if path[-1] == target:
                return len(path) - 1, path
            else:
                visited.append(path[-1])
                for edge in path[-1].get_edges():
                    next_node = edge.get_other_node(path[-1])
                    if next_node not in visited:
                        to_visit.put(path + [next_node])

        return None

    def __str__(self):
        return "DFS"

if __name__ == "__main__":
    graph = rgf.generate_oriented_graph(10, 3)
    print(DFS.start(graph, graph[0], graph[-1]))
    node1 = Node(0)
    node2 = Node(1)
    node3 = Node(2)
    node4 = Node(3)
    edge1 = Edge(node1, node2, 1, True)
    edge2 = Edge(node2, node3, 1, True)
    edge3 = Edge(node3, node4, 1, True)
    node1.add_edge(edge1)
    node2.add_edge(edge2)
    node3.add_edge(edge3)
    graph = [node1, node2, node3, node4]
    print([str(x) for x in DFS.start(graph, node1, node4)])