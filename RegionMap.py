import numpy
from Graph import Graph, Vertex
from ReadCSV import import_csv_distance_file, to_dictionary

dl = import_csv_distance_file('resources/WGUPS Distance Table.csv')

distance_matrix = dl

locations = []
for row in distance_matrix:
    locations.append(row[0])
    del row[0]
for i in range(len(distance_matrix)):
    for j in range(i + 1):
        t = distance_matrix[i][j]
        distance_matrix[j][i] = t
for row in distance_matrix:
    print(row)

g = Graph()

for loc in locations:
    g.add_vertex(Vertex(loc))

for vert in g.adjacency_dict.keys():
    for vert2 in g.adjacency_dict.keys():
        g.add_d_edge(vert, vert2, dl[locations.index(vert.label)][locations.index(vert2.label)])

for k, v in g.adjacency_dict.items():
    print('--')
    print(k.label)
    for i in v:
        print(i.label)

for k, v in g.edge_weights.items():
    print('Distance from {} to {}: {}'.format(k[0].label, k[1].label, v))


priority_list_locations = ()
