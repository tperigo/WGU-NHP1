import operator

from Database import print_package_table
from Graph import dsp, gsp, print_gsp, print_priority_gsp

from ReadCSV import import_csv_package_file, import_csv_distance_file
from RegionMap2 import create_map

pf = import_csv_package_file('resources/WGUPS Package File.csv')

# distance_table = import_csv_distance_file('resources/WGUPS Distance Table.csv')

# print_package_table(pf)

# Get priority packages
all_destinations = []
priority_queue = []
priority_destinations = []

for b in pf:
    if b is not None:
        for i in b:
            loc = str(i[1].get_address()) + ' ' + str(i[1].get_zip_code())
            all_destinations.append(loc)
            if i[1].get_deadline() != 'EOD':
                priority_queue.append(i[1])
                priority_destinations.append(loc)

for d in priority_destinations:
    print(d)

g = create_map()

# gsp(list(g.adjacency_list.keys())[0], list(g.adjacency_list.keys())[3])

for d in priority_destinations:
    for v in g.adjacency_list:
        if d == v.label:
            v.has_delivery = True

for k, v in g.adjacency_list.items():
    print(k.label, k.has_delivery)
print('--')

route = []
distance_moved = 0.0
v1 = print_priority_gsp(g, list(g.adjacency_list.keys())[0])
route.append(v1)

print_gsp(g, v1)

v2 = print_priority_gsp(g, v1)
route.append(v2)

v3 = print_priority_gsp(g, v2)
route.append(v3)





print('--')
for i in route:
    print(i.label)

# tsp_nn(g, list(g.adjacency_list.keys())[0])

