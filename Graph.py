import operator


class Vertex:
    def __init__(self, label):
        self.label = label
        self.distance = float('inf')
        self.pred_vertex = None
        self.visited = False


class Graph:
    def __init__(self):
        self.adjacency_list = {}
        self.edge_weights = {}

    def add_vertex(self, v):
        self.adjacency_list[v] = []

    # Add directional edge from A to B and its weight
    def add_directed_edge(self, a, b, w=1.0):
        self.edge_weights[(a, b)] = w
        self.adjacency_list[a].append(b)

    # Add undirected edge between A and B and its weight
    def add_undirected_edge(self, a, b, w=1.0):
        self.add_directed_edge(a, b, w)
        self.add_directed_edge(b, a, w)


def dsp(g, start_vertex):
    # Put all vertices in an unvisited queue.
    unvisited_queue = []
    for current_vertex in g.adjacency_list:
        unvisited_queue.append(current_vertex)

    # start_vertex has a distance of 0 from itself
    start_vertex.distance = 0

    # One vertex is removed with each iteration; repeat until the list is
    # empty.
    while len(unvisited_queue) > 0:

        # Visit vertex with minimum distance from start_vertex
        smallest_index = 0
        for i in range(1, len(unvisited_queue)):
            if unvisited_queue[i].distance < unvisited_queue[smallest_index].distance:
                smallest_index = i
        current_vertex = unvisited_queue.pop(smallest_index)

        # Check potential path lengths from the current vertex to all neighbors.
        for adj_vertex in g.adjacency_list[current_vertex]:
            edge_weight = g.edge_weights[(current_vertex, adj_vertex)]
            alternative_path_distance = float(current_vertex.distance) + float(edge_weight)

            # If shorter path from start_vertex to adj_vertex is found,
            # update adj_vertex's distance and predecessor
            if alternative_path_distance < adj_vertex.distance:
                adj_vertex.distance = alternative_path_distance
                adj_vertex.pred_vertex = current_vertex


def gsp(start_vertex, end_vertex):
    # Start from end_vertex and build the path backwards.
    path = ""
    current_vertex = end_vertex
    while current_vertex is not start_vertex:
        path = " -> " + str(current_vertex.label) + str(current_vertex.distance) + path
        current_vertex = current_vertex.pred_vertex
    path = start_vertex.label + path
    return path


def nearest_neighbor(g, start_vertex):
    dsp(g, start_vertex)
    min_distance = float('inf')
    nearest_v = start_vertex

    for v in g.adjacency_list:
        if v.pred_vertex is None and v is not start_vertex and v.visited is not True:
            print("A to %s: no path exists" % v.label)
        else:
            if min_distance > v.distance != 0:
                min_distance = v.distance
                nearest_v = v
    return nearest_v


def tsp_nn(g, start_vertex):
    first_vertex = start_vertex
    total_miles = 0.0
    total_locations = len(g.adjacency_list)
    # Start
    print("---Route Start---")
    print(first_vertex.label, '- {:0.1f}'.format(total_miles))
    first_vertex.visited = True

    # Find Nearest city to Start
    current_vertex = nearest_neighbor(g, first_vertex)
    total_miles += current_vertex.distance
    current_vertex.visited = True
    print(current_vertex.label, '- {:0.1f}'.format(total_miles))

    # Find nearest neighbor
    while total_locations > 2:
        next_v = nearest_neighbor(g, current_vertex)
        total_miles += next_v.distance
        # del region_map.adjacency_list[current_vertex]
        current_vertex.visited = True
        print(next_v.label, '- {:0.1f}'.format(total_miles))
        current_vertex = next_v
        total_locations -= 1

    # Return to Hub
    # TODO - Check DSP from last to HUB
    total_miles += float(g.edge_weights[current_vertex, start_vertex])
    current_vertex.visited = True
    print(start_vertex.label, '- {:0.1f}'.format(total_miles))
    print("---Route Complete---")
