from node import Node
from edge import Edge


def find_euler_cycle(graph: list[Node]):
    for node in graph:
        if len(node.get_edges()) % 2 != 0:
            return None
    cycle = []
    start_node = graph[0]
    current_node = start_node
    visited_node = set()
    while True:
        next_nodes = [edge.get_other_node(current_node) for edge in current_node.get_edges()]
        next_nodes = list(filter(lambda x: x, next_nodes))
        if len(visited_node.intersection(next_nodes))\
                == len(next_nodes):
            cycle.append(current_node)
            if current_node == start_node:
                break
            current_node = cycle[-2]
        else:
            find_next_node = False
            for edge in current_node.get_edges():
                node = edge.get_other_node(current_node)
                if node and node not in visited_node:
                    visited_node.add(node)
                    next_node = edge.get_other_node(current_node)
                    cycle.append(current_node)
                    current_node = next_node
                    find_next_node = True
                    break
            if not find_next_node:
                return None
    return cycle


if __name__ == "__main__":
    node1 = Node(0)
    node2 = Node(1)
    node3 = Node(2)
    edge1 = Edge(node3, node1, 1, True)
    node3.add_edge(edge1)
    node1.add_edge(edge1)
    edge2 = Edge(node1, node2, 2, True)
    node1.add_edge(edge2)
    node2.add_edge(edge2)
    edge3 = Edge(node2, node3, 1, True)
    node2.add_edge(edge3)
    node3.add_edge(edge3)
    print([str(x) for x in find_euler_cycle([node1, node2, node3])])