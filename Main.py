import operator

from Database import print_package_table
from Graph import dsp, gsp, print_gsp, print_priority_gsp, tsp_nd, tsp_nn

from ReadCSV import import_csv_package_file, import_csv_distance_file
from RegionMap2 import create_map
from Truck import Truck

pf = import_csv_package_file('resources/WGUPS Package File.csv')

# distance_table = import_csv_distance_file('resources/WGUPS Distance Table.csv')



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

print('--')
for p in priority_queue:
    print(p.get_package_id(), p.get_address(), p.get_zip_code(), p.get_status())

g = create_map()

# gsp(list(g.adjacency_list.keys())[0], list(g.adjacency_list.keys())[3])

for d in priority_destinations:
    for v in g.adjacency_list:
        if d == v.label:
            v.has_delivery = True


print('--')


# v1 = print_gsp(g, list(g.adjacency_list.keys())[0])


# tsp_nn(g, list(g.adjacency_list.keys())[0])
print('--')
# dsp(g, list(g.adjacency_list.keys())[0])
truck_001 = Truck('Bob')
for package in priority_queue:
    truck_001.load_package(package)

print('-loaded-')
for p in priority_queue:
    print(p.get_package_id(), p.get_address(), p.get_zip_code(), p.get_status())


tsp_nd(g, list(g.adjacency_list.keys())[0], len(set(priority_destinations)), truck_001)


print_package_table(pf)