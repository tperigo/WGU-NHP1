from Database import print_package_table

from ReadCSV import import_csv_package_file, import_csv_distance_file
from RegionMap2 import create_map

pf = import_csv_package_file('resources/WGUPS Package File.csv')

# distance_table = import_csv_distance_file('resources/WGUPS Distance Table.csv')

# print_package_table(pf)

# Get priority packages
priority_queue = []
priority_locations = []

all_locations = []

for b in pf:
    if b is not None:
        for i in b:
            loc = str(i[1].get_address()) + ' ' + str(i[1].get_zip_code())
            all_locations.append(loc)
            if i[1].get_deadline() != 'EOD':
                priority_queue.append(i[1])
                priority_locations.append(loc)

g = create_map()

# tsp_nn(g, list(g.adjacency_list.keys())[0])
