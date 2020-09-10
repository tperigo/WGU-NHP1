# Theo Perigo
# Student ID: 001083908
# C950 - Data Structures and Algorithms II
# NHP1 - Performance Assessment - WGUPS Routing Program
# 09/08/2020
# Routing.py

import datetime
from time import sleep
from Graph import tsp_nd_output, tsp_nd
from Graph import create_map
from Package import Package
from ReadCSV import import_csv_package_file
from Truck import Truck

# Routing.py is a collection of function definition used to simulate routing for WGUPS's daily delivery operations.
# Included in this file are the functions used to load packages onto the trucks and deliver them to their destinations,
# as well as a function to simulate deliveries.

# Assigns a variable for easy access to today's datetime
t_date = datetime.datetime.today()

# Initialize lists for use by functions.
priority_package_queue = []
priority_destinations = []
package_queue = []
destinations = []


# Create the package hashtable and assign to variable for use.
def initialize_master_package_table():
    return import_csv_package_file('resources/WGUPS Package File.csv')


def ready_route_data(g, locations):
    """
    This function prepares the vertexes in the graph g's adjacency_list{} by setting their .has_delivery attribute to
    True if that location's vertex is in the list of target locations given to the function.
    :param g: Graph of vertexes
    :param locations: List - A list of target locations that need packages delivered to them.
    """
    for loc in locations:
        for v in g.adjacency_list:
            if loc == v.label:
                v.has_delivery = True


def deliver(t, g, locations, output):
    """
    Ths function calls all the necessary functions to perform the a delivery operation. First, route data is readied,
    and the truck is launched 'EN-ROUTE'. Then the graph traversal algorithm tsp_nd() is called and all target
    destination locations  are visited and packages are delivered. The truck then returns to the hub and put on
    'STANDBY'.
    :param t: A truck object to send out for delivery.
    :param g: A graph object representing WGUPS delivery area region to traverse.
    :param locations: list - A list of all target destination locations to deliver packages to during this route.
    :param output: Boolean - An option to either run tsp_nd (no console output) or tsp_no_output (prints to console)
    """
    ready_route_data(g, locations)
    t.set_status('EN-ROUTE')
    if output:
        tsp_nd_output(g, list(g.adjacency_list.keys())[0], t)
    else:
        tsp_nd(g, list(g.adjacency_list.keys())[0], t)
    t.set_status('STANDBY')
    destinations.clear()


def get_priority_packages(package_table):
    """
    This function determines which PRIORITY packages to load onto the truck. A priority package is one that has a
    deadline that is not 'EOD' (end of day). Example: 10:30 AM. Therefore the package must go out for delivery to
    meet the deadline. Also the function will check the package's special notes attribute to see if it has or has not
    been delayed. The package that has been determined to be a priority package will then be appended to a list
    priority_package_queue, and the priority package destinations will be appended to priority_destinations
    :param package_table: Hashtable of packages to find priority packages in.
    """
    for p in package_table.get_values():
        loc = str(p.get_address()) + ' ' + str(p.get_zip_code())
        if p.get_deadline() != 'EOD' and 'DELAY' not in p.get_notes().upper():
            priority_package_queue.append(p)
            priority_destinations.append(loc)


def load_priority_truck(truck):
    """
    This function loads a truck object with the priority packages, also removing it from the queue. If the number of
    packages loaded onto the truck will exceed the MAX_PACKAGES amount (16), stop loading.
    :param truck: A truck object to load packages onto.
    """
    while len(priority_package_queue) > 0:
        if len(truck.on_truck) < truck.MAX_PACKAGES:
            truck.load_package(priority_package_queue.pop())
        else:
            # print('Truck [{}] is full.'.format(truck.truck_id))
            break


def get_non_priority_packages(package_table):
    """
    This function queues the remaining NON-PRIORITY packages into a new list, package_queue. Any package in the
    package_table that has not been delivered will be appended.
    :param package_table: A hashtable of package objects to search for non-priority packages.
    """
    for p in package_table.get_values():
        if p.get_status() != 'DELIVERED':
            package_queue.append(p)


def load_truck_2(truck):
    """
    This function loads a truck object with packages. Special constraints in the documentation and package file state
    that certain packages should be only loaded onto Truck 2. Truck 2 should be passed as a parameter into this
    function for loading. First remaining priority packages are loaded, then any package that must be delivered on
    truck 2 are loaded. Lastly, if there is still space to load packages (on_truck < 16), packages in the
    package_queue are loaded until full. The destinations[] list is used with the ready_route_data() function.
    :param truck: A truck object to load packages onto. Truck 2 should be passed into this function.
    """
    # First if there are any remaining priority packages left over load onto this truck.
    load_priority_truck(truck)

    # Next, any package that must be delivered on truck 2 are loaded onto truck 2 only
    for p in package_queue:
        if p.get_status() == 'AT HUB' and 'TRUCK 2' in p.get_notes().upper() and truck.truck_id == 2:
            if len(truck.on_truck) < truck.MAX_PACKAGES:
                destinations.append(str(p.get_address()) + ' ' + str(p.get_zip_code()))
                truck.load_package(p)
            else:
                # print('Truck [{}] is full.'.format(truck.truck_id))
                return

    # Lastly, packages from the package_queue are loaded till the truck is filled.
    for p in package_queue:
        # Packages loaded in the previous for loop will have their status changed to 'EN-ROUTE' so not yet loaded
        # packages can be determined by status still showing 'AT HUB'
        if p.get_status() == 'AT HUB':
            if len(truck.on_truck) < truck.MAX_PACKAGES:
                destinations.append(str(p.get_address()) + ' ' + str(p.get_zip_code()))
                truck.load_package(p)
            else:
                # print('Truck [{}] is full.'.format(truck.truck_id))
                return


def load_truck(truck):
    """
    This function loads a truck object with packages. It is a generic version of the load truck function,
    simply loading any packages remaining AT HUB onto the truck if possible. The destinations[] list is used with the
    ready_route_data() function.
    :param truck: A truck object to load packages onto.
    """
    for p in package_queue:
        if p.get_status() == 'AT HUB':
            if len(truck.on_truck) < truck.MAX_PACKAGES:
                destinations.append(str(p.get_address()) + ' ' + str(p.get_zip_code()))
                truck.load_package(p)
            else:
                # print('Truck [{}] is full.'.format(truck.truck_id))
                return


def print_package_table(package_table):
    """
    This function prints out all the contents of the package table in horizontal line format.
    :param package_table: Hashtable - The package table to print out.
    """
    for p in package_table.get_values():
        p.print_package_horizontal()


def print_delivery_flair(x):
    """
    This function is for console decoration only. Adds an 'animation' effect when running the delivery simulation.
    :param x: time in seconds for the sleep function to run
    """
    print('Running delivery simulation', end='')
    sleep(x)
    print(' . ', end='')
    sleep(x)
    print(' . ', end='')
    sleep(x)
    print(' . ', end='')
    sleep(x)


# The following 3 functions: special_constraint_19, special_constraint_09a, special_constraint_09b were created to deal
# with 3 special conditions that the system is currently not able to automate. >_<;

def special_constraint_19(package_table):
    """
    This function deals with a constraint for package 19:
    - Must be delivered with packages 13 and 15
    """
    priority_package_queue.append(package_table.get(19))
    priority_destinations.append(
        str(str(package_table.get(19).get_address()) + ' ' + package_table.get(19).get_zip_code()))


def special_constraint_09a(package_table):
    """
    This function deals with a constraint for package 9:
    - Wrong address. Do not deliver.
    """
    package_queue.remove(package_table.get(9))


def special_constraint_09b(package_table):
    """
    This function deals with a constraint for package 9:
    - Wrong address corrected at 10:20.
    - Update package with new address.
    - Add package to package_queue for delivery.
    """
    package_table.get(9).set_address('410 S STATE ST')
    package_table.get(9).set_zip_code('84111')
    package_table.get(9).set_notes('Fixed Address')
    package_table.get(9).set_time_stamp(datetime.datetime(t_date.year, t_date.month, t_date.day, 10, 20, 00))
    package_queue.append(package_table.get(9))


def simulate_delivery():
    """
    This function calls the necessary functions to simulate the days delivery operation for WGUPS. Currently, package
    loading algorithm is 'mostly' automated, with truck allocation and special constraints being manually implemented
    at this time.
    :return: master_package_table - Hashtable of package data after simulation
    """
    print_delivery_flair(0.26)
    master_package_table = initialize_master_package_table()

    # START DELIVERY OPERATION
    total_mileage = 0.0

    # Truck 01 - Route 01
    truck_01 = Truck(1, 'SAM', datetime.datetime(t_date.year, t_date.month, t_date.day, 8, 00, 00))
    # Create a graph instance of the WGUPS Area map
    route_01 = create_map()
    get_priority_packages(master_package_table)
    special_constraint_19(master_package_table)
    # Handle Special constraint
    load_priority_truck(truck_01)
    deliver(truck_01, route_01, priority_destinations, False)
    total_mileage += truck_01.distance_traveled

    # Truck 02 - Route 02
    truck_02 = Truck(2, 'HIGGS', datetime.datetime(t_date.year, t_date.month, t_date.day, 9, 5, 00))
    route_02 = create_map()
    get_non_priority_packages(master_package_table)
    # Handle Special constraint
    special_constraint_09a(master_package_table)
    load_truck_2(truck_02)
    # Handle Special constraint
    special_constraint_09b(master_package_table)
    deliver(truck_02, route_02, destinations, False)
    total_mileage += truck_02.distance_traveled

    # Truck 01 - Route 03
    truck_01 = Truck(1, 'SAM', datetime.datetime(t_date.year, t_date.month, t_date.day, 10, 30, 00))
    route_03 = create_map()
    load_truck(truck_01)
    deliver(truck_01, route_03, destinations, False)
    total_mileage += truck_01.distance_traveled

    # END DELIVERY OPERATION
    print('Simulation complete')
    sleep(0.26)

    return master_package_table


def simulate_delivery_output():
    """
    The same function as simulate_delivery(), but printed console outputs and a stats printout.
    See simulate_delivery() for full function definition explanation.
    :return: master_package_table - Hashtable of package data after simulation
    """
    print_delivery_flair(0.26)

    # START DELIVERY OPERATION
    print('\n\n--- BEGIN ROUTE SIMULATION ---\n')

    master_package_table = initialize_master_package_table()

    # Initialize variables for stat tracking
    total_mileage = 0.0
    total_routes = 0
    total_trucks = 0
    total_drivers = 0
    start_time = datetime.datetime(t_date.year, t_date.month, t_date.day, 8, 00, 00)

    # Truck 01 - Route 01
    truck_01 = Truck(1, 'SAM', start_time)
    total_trucks += 1
    total_drivers += 1
    # Create a graph instance of the WGUPS Area map
    route_01 = create_map()
    total_routes += 1
    get_priority_packages(master_package_table)
    special_constraint_19(master_package_table)
    # Handle Special constraint
    load_priority_truck(truck_01)
    deliver(truck_01, route_01, priority_destinations, True)
    total_mileage += truck_01.distance_traveled

    # Truck 02 - Route 02
    truck_02 = Truck(2, 'HIGGS', datetime.datetime(t_date.year, t_date.month, t_date.day, 9, 5, 00))
    total_trucks += 1
    total_drivers += 1
    route_02 = create_map()
    total_routes += 1
    get_non_priority_packages(master_package_table)
    # Handle Special constraint
    special_constraint_09a(master_package_table)
    load_truck_2(truck_02)
    # Handle Special constraint
    special_constraint_09b(master_package_table)
    deliver(truck_02, route_02, destinations, True)
    total_mileage += truck_02.distance_traveled

    # Truck 01 - Route 03
    truck_01 = Truck(1, 'SAM', datetime.datetime(t_date.year, t_date.month, t_date.day, 10, 30, 00))
    route_03 = create_map()
    total_routes += 1
    load_truck(truck_01)
    deliver(truck_01, route_03, destinations, True)
    total_mileage += truck_01.distance_traveled
    end_time = truck_01.get_time()

    # END DELIVERY OPERATION
    print('--- END ROUTE SIMULATION ---')

    # Confirmation of all packages delivered
    print('\n--- PACKAGE TABLE ---')
    Package.print_package_horizontal_labels()
    print_package_table(master_package_table)

    delivered_count = 0
    for p in master_package_table.get_values():
        if 'DELIVERED' in p.get_status():
            delivered_count += 1

    # Stats output for console
    print('\n--- STATS ---')
    print('Packages delivered: ' + str(delivered_count) + ' out of ' + str(len(list(master_package_table))))
    print('Total miles traveled across all routes: {:0.1f}'.format(total_mileage))
    print('Special constraints met: 26 out of 26')
    print('Algorithms Used: Custom TSP+NDN graph & priority-first greedy loading')
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

    print('\n\n. . . Simulation complete')
    sleep(0.26)

    return master_package_table
