import datetime
from Graph import tsp_nd
from Graph import create_map
from ReadCSV import import_csv_package_file
from Truck import Truck

date = datetime.datetime.today()
priority_package_queue = []
priority_destinations = []
package_queue = []
destinations = []


def initialize_package_table():
    return import_csv_package_file('resources/WGUPS Package File.csv')


def ready_route_data(g, stops):
    for s in stops:
        for v in g.adjacency_list:
            if s == v.label:
                v.has_delivery = True


def deliver(t, g, l):
    ready_route_data(g, l)
    t.set_status('EN-ROUTE')
    tsp_nd(g, list(g.adjacency_list.keys())[0], len(set(l)), t)
    t.set_status('STANDBY')
    destinations.clear()


def get_priority_packages(package_table):
    for b in package_table:
        if b is not None:
            for i in b:
                loc = str(i[1].get_address()) + ' ' + str(i[1].get_zip_code())
                if i[1].get_deadline() != 'EOD' and 'DELAY' not in i[1].get_notes().upper():
                    priority_package_queue.append(i[1])
                    priority_destinations.append(loc)


def queue_remaining_package_data(package_table):
    for b in package_table:
        if b is not None:
            for i in b:
                if i[1].get_status() != 'DELIVERED':
                    package_queue.append(i[1])


def load_priority_truck(_truck):
    for package in priority_package_queue:
        if len(_truck.on_truck) < _truck.MAX_PACKAGES:
            _truck.load_package(package)
        else:
            print('Truck is full.')
            break


def load_truck_2(_truck):
    for p in package_queue:
        if p.get_status() == 'AT HUB' and p.get_deadline() != 'EOD':
            if len(_truck.on_truck) < _truck.MAX_PACKAGES:
                destinations.append(str(p.get_address()) + ' ' + str(p.get_zip_code()))
                _truck.load_package(p)


    for p in package_queue:
        if p.get_status() == 'AT HUB' and 'TRUCK 2' in p.get_notes().upper():
            if len(_truck.on_truck) < _truck.MAX_PACKAGES:
                destinations.append(str(p.get_address()) + ' ' + str(p.get_zip_code()))
                _truck.load_package(p)


    for p in package_queue:
        if p.get_status() == 'AT HUB':
            if len(_truck.on_truck) < _truck.MAX_PACKAGES:
                destinations.append(str(p.get_address()) + ' ' + str(p.get_zip_code()))
                _truck.load_package(p)



def load_remaining_truck(_truck):
    for p in package_queue:
        if p.get_status() == 'AT HUB':
            if len(_truck.on_truck) < _truck.MAX_PACKAGES:
                destinations.append(str(p.get_address()) + ' ' + str(p.get_zip_code()))
                _truck.load_package(p)
            else:
                print('Truck is full.')
                break


def print_package_table(package_table):
    for b in package_table:
        if b is not None:
            for i in b:
                i[1].print_package_horizontal()
        else:
            print(None)


def special_constraint_19(package_table):
    priority_package_queue.append(package_table.get(19))
    priority_destinations.append(
        str(str(package_table.get(19).get_address()) + ' ' + package_table.get(19).get_zip_code()))


def special_constraint_09a(package_table):
    package_queue.remove(package_table.get(9))


def special_constraint_09b(package_table):
    package_table.get(9).set_address('410 S STATE ST')
    package_table.get(9).set_zip_code('84111')
    package_queue.append(package_table.get(9))


master_package_table = initialize_package_table()


def simulate_delivery():
    total_mileage = 0.0

    # Truck 01 - Route 01
    truck_01 = Truck(1, 'SAM', datetime.datetime(date.year, date.month, date.day, 8, 00, 00))
    route_01 = create_map()
    get_priority_packages(master_package_table)
    special_constraint_19(master_package_table)
    load_priority_truck(truck_01)
    deliver(truck_01, route_01, priority_destinations)
    total_mileage += truck_01.distance_traveled

    # Truck 02 - Route 02
    truck_02 = Truck(2, 'HIGGS', datetime.datetime(date.year, date.month, date.day, 9, 5, 00))
    route_02 = create_map()
    queue_remaining_package_data(master_package_table)
    special_constraint_09a(master_package_table)
    load_truck_2(truck_02)
    deliver(truck_02, route_02, destinations)
    total_mileage += truck_02.distance_traveled

    # Truck 01 - Route 03
    truck_01 = Truck(1, 'SAM', datetime.datetime(date.year, date.month, date.day, 10, 30, 00))
    route_03 = create_map()
    special_constraint_09b(master_package_table)
    load_remaining_truck(truck_01)
    deliver(truck_01, route_03, destinations)
    total_mileage += truck_01.distance_traveled

    # Confirmation of all packages delivered
    print_package_table(master_package_table)
    print('\nTotal miles traveled across all routes: {}'.format(total_mileage))
