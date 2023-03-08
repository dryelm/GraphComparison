from edge import Edge
from node import Node

def find_hamilton_cycle(graph: list[Node]):
    # check if hamilton cycle exists
    for node in graph:
        if len(node.get_edges()) != len(graph) - 1:
            return None

    # find hamilton cycle
    cycle = []
    start_node = graph[0]
    current_node = start_node
    visited_edge = set()
    while True:
        if len(visited_edge.intersection(current_node.get_edges()))\
                == len(current_node.get_edges()):
            cycle.append(current_node)
            if current_node == start_node:
                break
            current_node = cycle[-2]
        else:
            find_next_edge = False
            for edge in current_node.get_edges():
                if edge not in visited_edge and\
                        edge.get_other_node(current_node):
                    visited_edge.add(edge)
                    next_node = edge.get_other_node(current_node)
                    cycle.append(current_node)
                    current_node = next_node
                    find_next_edge = True
                    break
            if not find_next_edge:
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
    print([str(x) for x in find_hamilton_cycle([node1, node2, node3])])
