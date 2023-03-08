from node import Node


class Edge:
    def __init__(self, v1: Node, v2: Node, cost, is_oriented):
        self.v1 = v1
        self.v2 = v2
        self.cost = cost
        self.is_oriented = is_oriented

    def get_cost(self):
        return self.cost

    def get_other_node(self, this_node):
        if self.is_oriented and this_node == self.v1:
            return self.v2
        elif not self.is_oriented:
            if this_node == self.v2:
                return self.v1

            if this_node == self.v1:
                return self.v2

        return False

    def __str__(self):
        return f"{str(self.v1)} --{self.cost}-{'>' if self.is_oriented else '-'} {str(self.v2)}"
