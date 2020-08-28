import numpy
from Graph import Graph
from ReadCSV import import_csv_distance_file, to_dictionary

dl = import_csv_distance_file('WGUPS Distance Table.csv')

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
    g.add_vertex(loc)

for loc in locations:
    for loc2 in locations:
        g.add_d_edge(loc, loc2, dl[locations.index(loc)][locations.index(loc2)])

print(g.adjacency_dict)
print(g.edge_weights.keys())
