from NHP1.Hashtable import import_csv_file, print_package_list, Hashtable
from NHP1.Package import Package

f = import_csv_file('WGUPS Package File.csv')

print_package_list(f)
print('--')
f[1].get_data().print_package()
f[1].get_data().set_deadline(2)
f[1].get_data().print_package()

# Git test comment
