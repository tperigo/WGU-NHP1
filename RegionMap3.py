import operator
from Graph import Graph, Vertex, dsp, gsp, nearest_neighbor, tsp_nn
from ReadCSV import import_csv_distance_file


def create_map(list):
    dl = import_csv_distance_file('resources/WGUPS Distance Table.csv')

    destinations = list
    distance_matrix = dl
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
            g.add_undirected_edge(vert, vert2, dl[locations.index(vert.label)][locations.index(vert2.label)])

    for dest in destinations:
        g.adjacency_list.pop(dest)

    return g
