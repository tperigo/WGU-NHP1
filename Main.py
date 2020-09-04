import operator
import random

from Database import print_package_table
from Graph import dsp, gsp, print_gsp, print_priority_gsp, tsp_nd, tsp_nn

from ReadCSV import import_csv_package_file, import_csv_distance_file
from RegionMap2 import create_map
from Truck import Truck

pf = import_csv_package_file('resources/WGUPS Package File.csv')
g = create_map()

# Get priority packages
all_destinations = []
priority_queue = []
priority_destinations = []

for b in pf:
    if b is not None:
        for i in b:
            loc = str(i[1].get_address()) + ' ' + str(i[1].get_zip_code())
            all_destinations.append(loc)
            if i[1].get_deadline() != 'EOD' and 'DELAY' not in i[1].get_notes().upper():
                priority_queue.append(i[1])
                priority_destinations.append(loc)




# Load truck
truck_01 = Truck('SAM')
for package in priority_queue:
    truck_01.load_package(package)

# Ready map data
for d in priority_destinations:
    for v in g.adjacency_list:
        if d == v.label:
            v.has_delivery = True


# Deliver Packages
truck_01.set_status('EN-ROUTE')
tsp_nd(g, list(g.adjacency_list.keys())[0], len(set(priority_destinations)), truck_01)
truck_01.set_status('STANDBY')
print(truck_01.on_truck)

# Reset Map Data
g2 = create_map()

remaining_packages = []
truck_02_destinations = []

for b in pf:
    if b is not None:
        for i in b:
            if i[1].get_status() != 'DELIVERED':

                remaining_packages.append(i[1])

truck_02 = Truck('HIGGS')

for p in remaining_packages:
    if p.get_deadline() != 'EOD' or 'TRUCK 2' in p.get_notes().upper():
        truck_02_destinations.append(str(p.get_address()) + ' ' + str(p.get_zip_code()))
        truck_02.load_package(p)


for p in remaining_packages:
    if p.get_status() != 'EN-ROUTE' and len(truck_02.on_truck) < truck_02.MAX_PACKAGES:
        if str(p.get_address()) + ' ' + str(p.get_zip_code()) not in truck_02_destinations:
            truck_02_destinations.append(str(p.get_address()) + ' ' + str(p.get_zip_code()))
            truck_02.load_package(p)

# Ready map data
for d in truck_02_destinations:
    for v in g2.adjacency_list:
        if d == v.label:
            v.has_delivery = True


truck_02.set_status('EN-ROUTE')
tsp_nd(g2, list(g2.adjacency_list.keys())[0], len(set(truck_02_destinations)), truck_02)
truck_02.set_status('STANDBY')
print(truck_02.on_truck)


g3 = create_map()
truck_01_destinations = []


for p in remaining_packages:
    if p.get_status() == 'AT HUB' and len(truck_01.on_truck) < truck_01.MAX_PACKAGES:
        truck_01_destinations.append(str(p.get_address()) + ' ' + str(p.get_zip_code()))
        truck_01.load_package(p)

# Ready map data
for d in truck_01_destinations:
    for v in g3.adjacency_list:
        if d == v.label:
            v.has_delivery = True

truck_01.set_status('EN-ROUTE')
tsp_nd(g3, list(g3.adjacency_list.keys())[0], len(set(truck_01_destinations)), truck_01)
truck_01.set_status('STANDBY')
print(truck_01.on_truck)

print_package_table(pf)

# TODO - That one package that has an address error
# TODO - Time / Total Mileage
# TODO - UI
# TODO - Clean up and Documentation
