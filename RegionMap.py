import operator
from Graph import Graph, Vertex, dsp, gsp, nearest_neighbor, tsp_nn
from ReadCSV import import_csv_distance_file


def create_map():
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

    g = Graph()

    vertex_0 = Vertex(locations[0])
    vertex_1 = Vertex(locations[1])
    vertex_2 = Vertex(locations[2])
    vertex_3 = Vertex(locations[3])
    vertex_4 = Vertex(locations[4])
    vertex_5 = Vertex(locations[5])
    vertex_6 = Vertex(locations[6])
    vertex_7 = Vertex(locations[7])
    vertex_8 = Vertex(locations[8])
    vertex_9 = Vertex(locations[9])
    vertex_10 = Vertex(locations[10])
    vertex_11 = Vertex(locations[11])
    vertex_12 = Vertex(locations[12])
    vertex_13 = Vertex(locations[13])
    vertex_14 = Vertex(locations[14])
    vertex_15 = Vertex(locations[15])
    vertex_16 = Vertex(locations[16])
    vertex_17 = Vertex(locations[17])
    vertex_18 = Vertex(locations[18])
    vertex_19 = Vertex(locations[19])
    vertex_20 = Vertex(locations[20])
    vertex_21 = Vertex(locations[21])
    vertex_22 = Vertex(locations[22])
    vertex_23 = Vertex(locations[23])
    vertex_24 = Vertex(locations[24])
    vertex_25 = Vertex(locations[25])
    vertex_26 = Vertex(locations[26])

    g.add_vertex(vertex_0)
    g.add_vertex(vertex_1)
    g.add_vertex(vertex_2)
    g.add_vertex(vertex_3)
    g.add_vertex(vertex_4)
    g.add_vertex(vertex_5)
    g.add_vertex(vertex_6)
    g.add_vertex(vertex_7)
    g.add_vertex(vertex_8)
    g.add_vertex(vertex_9)
    g.add_vertex(vertex_10)
    g.add_vertex(vertex_11)
    g.add_vertex(vertex_12)
    g.add_vertex(vertex_13)
    g.add_vertex(vertex_14)
    g.add_vertex(vertex_15)
    g.add_vertex(vertex_16)
    g.add_vertex(vertex_17)
    g.add_vertex(vertex_18)
    g.add_vertex(vertex_19)
    g.add_vertex(vertex_20)
    g.add_vertex(vertex_21)
    g.add_vertex(vertex_22)
    g.add_vertex(vertex_23)
    g.add_vertex(vertex_24)
    g.add_vertex(vertex_25)
    g.add_vertex(vertex_26)

    for vert in g.adjacency_list.keys():
        for vert2 in g.adjacency_list.keys():
            g.add_undirected_edge(vert, vert2, dl[locations.index(vert.label)][locations.index(vert2.label)])

    #
    # for k, v in g.adjacency_list.items():
    #     print('--')
    #     print(k.label)
    #     for i in v:
    #         print(i.label)
    #
    # for v in sorted(g.adjacency_list, key=operator.attrgetter("label")):
    #     if v.pred_vertex is None and v is not vertex_0:
    #         print("A to %s: no path exists" % v.label)
    #     else:
    #         print("A to %s: %s (total weight: %g)" % (v.label, gsp(vertex_0, v), v.distance))

    # tsp_nn(g, vertex_0)
