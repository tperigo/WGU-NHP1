# Theo Perigo
# Student ID: 001083908
# C950 - Data Structures and Algorithms II
# NHP1 - Performance Assessment - WGUPS Routing Program
# 09/08/2020
# Graph.py

import datetime
import operator
from ReadCSV import import_csv_distance_file


class Vertex:
    """
    This class defines a single vertex object. A vertex represents a point on a graph. A vertex has a label,
    a distance, a pred_vertex (previous vertex), tracks whether it has been visited with a boolean and tracks
    whether it is a delivery destination.
    """
    def __init__(self, label):
        """
        Initializes a vertex object
        :param label: string - The vertex's label/name.
        """
        self.label = label
        # Initialized as float('inf'), or 'infinity'. Used with DSP
        self.distance = float('inf')
        # Point to another vertex. Used with DSP
        self.pred_vertex = None
        # Boolean
        self.visited = False
        # Boolean
        self.has_delivery = False


class Graph:
    """
    This class defines a graph object and the functions used to manipulate it. A graph object is a type of data
    structure that represents a collection of vertexes connected by edges. Connected vertexes are kept track of in
    the adjacency_list dictionary, with the key being one vertex, and the values being all the vertexes it is
    adjacent to. The distance between them (edge weights) are kept in the edge_weights dictionary with the key being
    a tuple of vertexes and the value being the weight between them.
    """
    def __init__(self):
        """
        Initializes the graph object.
        """
        # Initializes an empty adjacency_list dictionary.
        self.adjacency_list = {}
        # Initializes an empty edge_weight dictionary.
        self.edge_weights = {}

    def add_vertex(self, v):
        """
        Adds a vertex to the graph via adding it as a key to the adjacency_list{}.
        :param v: Vertex to add
        """
        self.adjacency_list[v] = []

    def add_directed_edge(self, a, b, w=1.0):
        """
        Add a uni-directional edge from A to B and its weight. FROM A -> TO B. Tuple of (a, b) is added to
        edge_weights{} with w as the value. B is appended to A's list in the adjacency_list{} dictionary.
        :param a: From vertex
        :param b: To Vertex
        :param w: float - The weight or distance between the two vertexes. Default value is 1.0.
        """
        self.edge_weights[(a, b)] = w
        self.adjacency_list[a].append(b)

    def add_undirected_edge(self, a, b, w=1.0):
        """
        Add a undirected (bi-directional) edge between A and B and its weight. BETWEEN A <-> B. This is done by
        technically calling the add_directed_edge() function twice, one for A -> B and the weight, and the other for
        B->A and the weight
        :param a: First vertex
        :param b: Second vertex
        :param w: float - The weight or distance between the two vertexes. Default value is 1.0.
        :return:
        """
        self.add_directed_edge(a, b, w)
        self.add_directed_edge(b, a, w)


def create_map():
    """
    This function creates a graph representing the real world area map of the WGUPS's delivery region. First it
    imports the direction data from a given CVS file and parses the data into a list of unique delivery locations and
    a 2D adjacency matrix array of distances between each location. The list of locations are used to add vertexes to
    the graph representing the delivery locations. The distances in the matrix are then used to add undirected edges
    to the graph. This graph is then returned.

    :return: g: graph - A graph object representing the real world area map of the WGUPS's delivery region.
    """
    # Import and parse the CSV file to a list.
    distance_matrix = import_csv_distance_file('resources/WGUPS Distance Table.csv')
    # Initialize a list for delivery locations.
    locations = []
    # Initialize a graph object, g.
    g = Graph()
    # The first index in each row from the distance_matrix is a location. Add this to the locations list to use later.
    for row in distance_matrix:
        locations.append(row[0])
        del row[0]
    for i in range(len(distance_matrix)):
        # This function mirrors the bottom left triangle of the matrix to the upper right.
        for j in range(i + 1):
            t = distance_matrix[i][j]
            distance_matrix[j][i] = t
    # Add locations as vertexes to the graph
    for v in locations:
        g.add_vertex(Vertex(v))
    # Iterate for each vertex (location) in the graph's adjacency_list, and then for each vertex again per vertex to
    # add undirected edges to the graph. Weights are obtained by finding the corresponding indexes in the distance
    # matrix.
    for vert in g.adjacency_list.keys():
        for vert2 in g.adjacency_list.keys():
            g.add_undirected_edge(vert, vert2,
                                  distance_matrix[locations.index(vert.label)][locations.index(vert2.label)])
    return g


def dsp(g, start_vertex):
    """
    Ths method defines an implementation of Dijkstra's Shortest Path (DSP) for determining the shortest path from a
    start_vertex to each vertex in a graph 'g'. Dijkstra's algorithm initializes all vertices' distances to float(
    'inf') or infinity, initializes all vertices' predecessors to 0, and pushes all vertices to a queue of unvisited
    vertices. The algorithm then assigns the start vertex's distance with 0. While the queue is not empty,
    the algorithm pops the vertex with the shortest distance from the queue. For each adjacent vertex, the algorithm
    computes the distance of the path from the start vertex to the current vertex and continuing on to the adjacent
    vertex. If that path's distance is shorter than the adjacent vertex's current distance, a shorter path has been
    found. The adjacent vertex's current distance is updated to the distance of the newly found shorter path's
    distance, and vertex's predecessor pointer is pointed to the current vertex.

    SOURCE CODE: C960 zyBook 6.11 Algorithm: Dijkstra's Shortest Path.

    :param g: graph - Graph object with vertexes that will have distance and pred_vertex attributes modified as a
    result.
    :param start_vertex: vertex - Start vertex to find the shortest path for.
    """

    unvisited_queue = []
    # Add all location vertexes to the unvisited_queue[] list.
    for current_vertex in g.adjacency_list:
        unvisited_queue.append(current_vertex)

    # start_vertex has a distance of 0 from itself.
    start_vertex.distance = 0

    # Repeat while loop until the list is empty.
    while len(unvisited_queue) > 0:

        # Visit vertex with minimum distance from start_vertex.
        smallest_index = 0
        for i in range(1, len(unvisited_queue)):
            if unvisited_queue[i].distance < unvisited_queue[smallest_index].distance:
                smallest_index = i
        # One vertex is removed with each iteration
        current_vertex = unvisited_queue.pop(smallest_index)

        # Check potential path lengths from the current vertex to all neighbors.
        for adj_vertex in g.adjacency_list[current_vertex]:
            edge_weight = g.edge_weights[(current_vertex, adj_vertex)]
            alternative_path_distance = float(current_vertex.distance) + float(edge_weight)

            # If shorter path from start_vertex to adj_vertex is found, update adj_vertex's distance and predecessor.
            if alternative_path_distance < adj_vertex.distance:
                adj_vertex.distance = alternative_path_distance
                adj_vertex.pred_vertex = current_vertex


def nearest_delivery(g, start_vertex):
    """

    :param g:
    :param start_vertex:
    :return:
    """
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
    print('--- Route Start on ' + datetime.datetime.strftime(truck.get_time(), '%H:%M:%S') + ' ---')
    print('Truck 0{} - {} - Departing {} - Current mileage: {:0.1f}'.format(truck.truck_id, truck.driver,
                                                                            first_vertex.label, total_miles))
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
        print('  * Package ID {} has been delivered to {} *'.format(p.get_package_id(), current_vertex.label))
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
            print('  * Package ID {} has been delivered to {} *'.format(p.get_package_id(), next_v.label))
        unload_list.clear()

        current_vertex = next_v
        number_of_stops -= 1

    # Return to Hub
    total_miles += float(g.edge_weights[current_vertex, start_vertex])
    current_vertex.visited = True
    print('Current location:', start_vertex.label, '- Total mileage: {:0.1f}'.format(total_miles))
    truck.travel(float(g.edge_weights[current_vertex, start_vertex]))

    print('--- Route Complete on ' + datetime.datetime.strftime(truck.get_time(), '%H:%M:%S') + ' ---')
    print('')


def tsp_nd_bg(g, start_vertex, number_of_stops, truck):
    first_vertex = start_vertex
    total_miles = 0.0

    # Start
    first_vertex.visited = True

    # Find Nearest delivery to Start
    current_vertex = nearest_delivery(g, first_vertex)
    total_miles += current_vertex.distance
    current_vertex.visited = True
    truck.travel(current_vertex.distance)
    unload_list = []
    for p in truck.on_truck:
        if str(p.get_address() + ' ' + p.get_zip_code()) == current_vertex.label:
            unload_list.append(p)

    for p in unload_list:
        truck.deliver_package(p)
    unload_list.clear()

    # Find nearest delivery again
    while number_of_stops >= 2:
        next_v = nearest_delivery(g, current_vertex)
        total_miles += next_v.distance
        next_v.visited = True
        truck.travel(next_v.distance)
        for p in truck.on_truck:
            if str(p.get_address() + ' ' + p.get_zip_code()) == next_v.label:
                unload_list.append(p)

        for p in unload_list:
            truck.deliver_package(p)
        unload_list.clear()

        current_vertex = next_v
        number_of_stops -= 1

    # Return to Hub
    total_miles += float(g.edge_weights[current_vertex, start_vertex])
    current_vertex.visited = True

    truck.travel(float(g.edge_weights[current_vertex, start_vertex]))


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
