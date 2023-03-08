import queue
from queue import Queue
from node import Node
from edge import Edge


class BFS:
    @staticmethod
    def start(graph: list[Node], start_node: Node, target: Node):
        visited = []
        to_visit = Queue()
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
        return "BFS"

if __name__ == "__main__":
    node1 = Node(0)
    node2 = Node(1)
    node3 = Node(2)
    edge1 = Edge(node1, node2, 1, True)
    edge2 = Edge(node2, node3, 1, True)
    node1.add_edge(edge1)
    node2.add_edge(edge2)
    print([str(x) for x in BFS.start([node1, node2, node3], node1, node3)])
