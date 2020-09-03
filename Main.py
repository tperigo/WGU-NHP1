from Database import print_package_table

from ReadCSV import import_csv_package_file, import_csv_distance_file
from RegionMap import create_map

pf = import_csv_package_file('resources/WGUPS Package File.csv')

# distance_table = import_csv_distance_file('resources/WGUPS Distance Table.csv')

# print_package_table(pf)

# Get priority packages
priority_queue = []
priority_locations = []
for b in pf:
    if b is not None:
        for i in b:
            if i[1].get_deadline() != 'EOD':
                priority_queue.append(i[1])
                priority_locations.append(i[1].get_address())


print(priority_locations)

create_map()
