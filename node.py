class Node:
    def __init__(self, name):
        self.name = name
        self._edges = []

    def get_edges(self):
        return self._edges

    def remove_edge(self, edge):
        self._edges.remove(edge)

    def add_edge(self, edge):
        self._edges.append(edge)

    def __str__(self):
        return f"{self.name}"

    def __le__(self, other):
        return self.name <= other.name

    def __lt__(self, other):
        return self.name < other.name










