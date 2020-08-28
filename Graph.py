class Graph:
    def __init__(self):
        self.adjacency_dict = {}
        self.edge_weights = {}

    def add_vertex(self, v):
        self.adjacency_dict[v] = []

    # Add directional edge from A to B and its weight
    def add_d_edge(self, a, b, w=1.0):
        self.edge_weights[(a, b)] = w
        self.adjacency_dict[a].append(b)

    # Add undirected edge between A and B and its weight
    def add_u_edge(self, a, b, w=1.0):
        self.add_d_edge(a, b, w)
        self.add_d_edge(b, a, w)
