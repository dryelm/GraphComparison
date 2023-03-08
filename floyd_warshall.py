from node import Node
from edge import Edge

class FloydWarshall:
    @staticmethod
    # using floyd-warshall algo returns shortest path from start to target
    def start(graph: list[Node], start_node: Node, target: Node):
        distances = {node: {node: float("inf") for node in graph} for node in graph}
        paths = {node: {node: [] for node in graph} for node in graph}

        for node in graph:
            for edge in node.get_edges():
                distances[node][edge.get_other_node(node)] = edge.get_cost()
                paths[node][edge.get_other_node(node)] = [node, edge.get_other_node(node)]

        for k in graph:
            for i in graph:
                for j in graph:
                    if distances[i][k] + distances[k][j] < distances[i][j]:
                        distances[i][j] = distances[i][k] + distances[k][j]
                        paths[i][j] = paths[i][k] + paths[k][j][1:]
        # check for negative cycles
        for k in graph:
            for i in graph:
                for j in graph:
                    if distances[i][k] + distances[k][j] < distances[i][j]:
                        return None
        return (distances[start_node][target], paths[start_node][target])

    def __str__(self):
        return "Floyd-Warshall"