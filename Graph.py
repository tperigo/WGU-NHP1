import datetime
import operator
from ReadCSV import import_csv_distance_file


class Vertex:
    def __init__(self, label):
        self.label = label
        self.distance = float('inf')
        self.pred_vertex = None
        self.visited = False
        self.has_delivery = False
        self.next = None


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


def print_gsp(g, v):
    dsp(g, v)
    for v in sorted(g.adjacency_list, key=operator.attrgetter("distance")):
        if v.pred_vertex is None and v is not list(g.adjacency_list.keys())[0]:
            print("A to %s: no path exists" % v.label)
        else:
            print("A to %s: %s (total distance: %g)" % (v.label, gsp(list(g.adjacency_list.keys())[0], v), v.distance))


def nearest_delivery(g, start_vertex):
    dsp(g, start_vertex)
    min_distance = float('inf')
    nearest_v = start_vertex

    for v in g.adjacency_list:
        if v.pred_vertex is None and v is not start_vertex and v.visited is not True:
            print("A to %s: no path exists" % v.label)
        else:
            if min_distance > v.distance != 0 and v.has_delivery:
                min_distance = v.distance
                nearest_v = v
    return nearest_v


def tsp_nd(g, start_vertex, number_of_stops, truck):
    first_vertex = start_vertex
    total_miles = 0.0

    # Start
    print("---Route Start---")
    print(truck.get_time())
    print('Current location:', first_vertex.label, '- Current mileage: {:0.1f}'.format(total_miles))
    first_vertex.visited = True

    # Find Nearest delivery to Start
    current_vertex = nearest_delivery(g, first_vertex)
    total_miles += current_vertex.distance
    current_vertex.visited = True
    print('Current location:', current_vertex.label, '- Current mileage: {:0.1f}'.format(total_miles))
    truck.travel(current_vertex.distance)
    unload_list = []
    for p in truck.on_truck:
        if str(p.get_address() + ' ' + p.get_zip_code()) == current_vertex.label:
            unload_list.append(p)

    for p in unload_list:
        truck.deliver_package(p)
        print('** Package ID {} has been delivered to {} **'.format(p.get_package_id(), current_vertex.label))
    unload_list.clear()

    # Find nearest delivery again
    while number_of_stops >= 2:
        next_v = nearest_delivery(g, current_vertex)
        total_miles += next_v.distance
        next_v.visited = True
        print('Current location:', next_v.label, '- Current mileage: {:0.1f}'.format(total_miles))
        truck.travel(next_v.distance)
        for p in truck.on_truck:
            if str(p.get_address() + ' ' + p.get_zip_code()) == next_v.label:
                unload_list.append(p)

        for p in unload_list:
            truck.deliver_package(p)
            print('** Package ID {} has been delivered to {} **'.format(p.get_package_id(), next_v.label))
        unload_list.clear()

        current_vertex = next_v
        number_of_stops -= 1

    # Return to Hub
    total_miles += float(g.edge_weights[current_vertex, start_vertex])
    current_vertex.visited = True
    print('Current location:', start_vertex.label, '- Total mileage: {:0.1f}'.format(total_miles))
    truck.travel(float(g.edge_weights[current_vertex, start_vertex]))

    print("---Route Complete---" + datetime.datetime.strftime(truck.get_time(), '%H:%M:%S'))


# Checks if locations are in the graph
def check_locations(_list, _graph):
    for location in _list:
        print("Checking " + location)
        found = False
        for v in _graph.adjacency_list:
            if location == v.label:
                print("Match found || " + location + ' || ' + v.label)
                found = True
                break
            else:
                found = False
        if found is False:
            for v in _graph.adjacency_list:
                print("-Error || " + location + ' |x| ' + v.label)


def create_map():
    distance_matrix = import_csv_distance_file('resources/WGUPS Distance Table.csv')
    locations = []
    g = Graph()

    for row in distance_matrix:
        locations.append(row[0])
        del row[0]
    for i in range(len(distance_matrix)):
        for j in range(i + 1):
            t = distance_matrix[i][j]
            distance_matrix[j][i] = t

    for v in locations:
        g.add_vertex(Vertex(v))

    for vert in g.adjacency_list.keys():
        for vert2 in g.adjacency_list.keys():
            g.add_undirected_edge(vert, vert2,
                                  distance_matrix[locations.index(vert.label)][locations.index(vert2.label)])
    return g