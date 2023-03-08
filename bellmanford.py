from node import Node
from edge import Edge

class BellmanFord:
    # using bellman-ford algo returns shortest path from start to target
    @staticmethod
    def start(graph: list[Node], start: Node, target):
        distances = {node: [float("inf"), []] for node in graph}
        distances[start] = [0, [start]]
        for i in range(len(graph) - 1):
            for node in graph:
                for edge in node.get_edges():
                    next_node = edge.get_other_node(node)
                    if distances[node][0] + edge.get_cost() \
                            < distances[next_node][0]:
                        distances[next_node][0] = \
                            distances[node][0] + edge.get_cost()
                        distances[next_node][1] = distances[node][1] + [next_node]

        for node in graph:
            for edge in node.get_edges():
                next_node = edge.get_other_node(node)
                if distances[node][0] + edge.get_cost() < distances[next_node][0]:
                    return None
        return distances[target][0], distances[target][1]

    def __str__(self):
        return "Bellman-Ford"


if __name__ == "__main__":

    node1 = Node(0)
    node2 = Node(1)
    node3 = Node(2)
    edge1 = Edge(node3, node1, 1, True)
    node3.add_edge(edge1)
    edge2 = Edge(node1, node2, 2, True)
    node1.add_edge(edge2)
    edge3 = Edge(node2, node3, 1, True)
    node2.add_edge(edge3)
    print([str(x) for x in BellmanFord.start([node1, node2, node3], node2, node3)])
