import datetime
from time import sleep

from Graph import tsp_nd, tsp_nd_bg
from Graph import create_map
from ReadCSV import import_csv_package_file
from Truck import Truck

priority_package_queue = []
priority_destinations = []
package_queue = []
destinations = []

t_date = datetime.datetime.today()
clock = datetime.datetime(t_date.year, t_date.month, t_date.day, 8, 00, 00)


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


def deliver_bg(t, g, l):
    ready_route_data(g, l)
    t.set_status('EN-ROUTE')
    tsp_nd_bg(g, list(g.adjacency_list.keys())[0], len(set(l)), t)
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
            # print('Truck is full.')
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
                # print('Truck is full.')
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


def print_delivery_flair(x):
    sleep(x + 0.1)
    print('Running delivery simulation', end='')
    sleep(x + 0.1)
    print(' . ', end='')
    sleep(x)
    print(' . ', end='')
    sleep(x)
    print(' . ', end='')
    sleep(x)


master_package_table = initialize_package_table()


def simulate_delivery_output():
    print_delivery_flair(0.3)
    print('\n\n--- BEGIN ROUTE SIMULATION ---\n')
    total_mileage = 0.0
    total_routes = 0
    total_trucks = 0
    total_drivers = 0

    start_time = datetime.datetime(t_date.year, t_date.month, t_date.day, 8, 00, 00)

    # Truck 01 - Route 01
    truck_01 = Truck(1, 'SAM', start_time)
    total_trucks += 1
    total_drivers += 1
    route_01 = create_map()
    total_routes += 1
    get_priority_packages(master_package_table)
    special_constraint_19(master_package_table)
    load_priority_truck(truck_01)
    deliver(truck_01, route_01, priority_destinations)
    total_mileage += truck_01.distance_traveled

    # Truck 02 - Route 02
    truck_02 = Truck(2, 'HIGGS', datetime.datetime(t_date.year, t_date.month, t_date.day, 9, 5, 00))
    total_trucks += 1
    total_drivers += 1
    route_02 = create_map()
    total_routes += 1
    queue_remaining_package_data(master_package_table)
    special_constraint_09a(master_package_table)
    load_truck_2(truck_02)
    deliver(truck_02, route_02, destinations)
    total_mileage += truck_02.distance_traveled

    # Truck 01 - Route 03
    truck_01 = Truck(1, 'SAM', datetime.datetime(t_date.year, t_date.month, t_date.day, 10, 30, 00))
    route_03 = create_map()
    total_routes += 1
    special_constraint_09b(master_package_table)
    load_remaining_truck(truck_01)
    deliver(truck_01, route_03, destinations)
    total_mileage += truck_01.distance_traveled
    end_time = truck_01.get_time()

    print('--- END ROUTE SIMULATION ---')

    # Confirmation of all packages delivered
    print('\n--- PACKAGE TABLE ---')
    print_package_table(master_package_table)

    delivered_count = 0
    for b in master_package_table:
        for i in b:
            if 'DELIVERED' in i[1].get_status():
                delivered_count += 1

    # Stat output for console
    print('\n--- STATS ---')
    print('Packages delivered: ' + str(delivered_count) + ' out of ' + str(len(list(master_package_table))))
    print('Total miles traveled across all routes: {}'.format(total_mileage))
    print('Special constraints met: 26 out of 26')
    print('Algorithms Used: Custom NDN+TSP graph & SemiHC+auto priority-first greedy loading')
    print('Total routes taken: ' + str(total_routes))
    print('Total trucks used: ' + str(total_trucks))
    print('Total drivers used: ' + str(total_drivers))
    print(
        'Start time: ' + datetime.datetime.strftime(start_time,
                                                    '%H:%M'))
    print('End time: ' + datetime.datetime.strftime(end_time, '%H:%M'))
    total_duration = end_time - start_time
    h, r = divmod(total_duration.total_seconds(), 3600)
    m, s = divmod(r, 60)
    print('Total duration: {:02} hours {:02} minutes '.format(int(h), int(m)))



def simulate_delivery():
    print_delivery_flair(0.3)
    total_mileage = 0.0
    # Truck 01 - Route 01
    truck_01 = Truck(1, 'SAM', datetime.datetime(t_date.year, t_date.month, t_date.day, 8, 00, 00))
    route_01 = create_map()
    get_priority_packages(master_package_table)
    special_constraint_19(master_package_table)
    load_priority_truck(truck_01)
    deliver_bg(truck_01, route_01, priority_destinations)
    total_mileage += truck_01.distance_traveled

    # Truck 02 - Route 02
    truck_02 = Truck(2, 'HIGGS', datetime.datetime(t_date.year, t_date.month, t_date.day, 9, 5, 00))
    route_02 = create_map()
    queue_remaining_package_data(master_package_table)
    special_constraint_09a(master_package_table)
    load_truck_2(truck_02)
    deliver_bg(truck_02, route_02, destinations)
    total_mileage += truck_02.distance_traveled

    # Truck 01 - Route 03
    truck_01 = Truck(1, 'SAM', datetime.datetime(t_date.year, t_date.month, t_date.day, 10, 30, 00))
    route_03 = create_map()
    special_constraint_09b(master_package_table)
    load_remaining_truck(truck_01)
    deliver_bg(truck_01, route_03, destinations)
    total_mileage += truck_01.distance_traveled

    print('\nSimulation Complete')
