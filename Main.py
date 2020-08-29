from Database import print_package_table

from ReadCSV import import_csv_package_file, import_csv_distance_file

pf = import_csv_package_file('resources/WGUPS Package File.csv')

# distance_table = import_csv_distance_file('resources/WGUPS Distance Table.csv')

print_package_table(pf)
print('--')

priority_queue = []

# Get priority packages
for b in pf:
    if b is not None:
        for i in b:
            if i[1].get_deadline() != 'EOD':
                priority_queue.append(i[1])

for p in priority_queue:
    p.print_package()