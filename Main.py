from Database import print_package_table

from ReadCSV import import_csv_package_file, import_csv_distance_file

pf = import_csv_package_file('WGUPS Package File.csv')

# distance_table = import_csv_distance_file('WGUPS Distance Table.csv')

print_package_table(pf)
print('--')

print_package_table(pf)

