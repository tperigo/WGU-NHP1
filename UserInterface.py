# Theo Perigo
# Student ID: 001083908
# C950 - Data Structures and Algorithms II
# NHP1 - Performance Assessment - WGUPS Routing Program
# 09/08/2020
# UserInterface.py

import datetime
from time import sleep

from Hashtable import Hashtable
from Package import Package
from Routing import simulate_delivery, simulate_delivery_output

# Assigns a variable for easy access to today's datetime
t_date = datetime.datetime.today()


def UserInterface():
    """
    Starts the WGUPS command line interface. Calls an intro() function, proceeded by the main_menu() function.
    """
    intro()
    main_menu()


def intro():
    """ Prints a title intro to the console. """
    print('\n------====== WGUPS Command Line Interface | ver. 0.9.1 BETA ======------')


def main_menu():
    """
    Prints the main menu with numbered options to the console. The user can then input a number to return a
    specified function.
    :return: mm_options(user_input): Calls a function based on the users input string.
    """
    print('\n------====== MAIN MENU ======------\n')
    print("What would you like to do?")
    print('    1. Look up package(s)\n'
          '    2. Run full day delivery simulation\n'
          '    3. View package table status at a specified time\n'
          '    4. Exit the program\n')
    user_input = input('Enter a number: ')
    return mm_options(user_input)


def mm_options(user_input):
    """
    Calls a function based on the users input string.
    If an invalid input is entered, prints a warning and calls main_menu() again.
    :param user_input: string - User input string for desired option
    """
    if user_input == '1':
        print('\n------====== PACKAGE LOOKUP ======------')
        snapshot = create_snapshot()
        run_lookup(snapshot)
    elif user_input == '2':
        run_simulation()
    elif user_input == '3':
        snapshot_package_table()
    elif user_input == '4':
        run_exit()
    else:
        print('\n    Invalid input. Please try again...')
        main_menu()


def run_exit():
    """ Exits the program. """
    print('\n    Exiting program...')
    sleep(.26)
    exit()


def run_lookup(snapshot):
    """
    Runs the package lookup function. This function takes a user input string to specify a type of package attribute
    to look up at the previously given time. The user then enters the desired package attribute and the program will
    search the master_package_table HashTable and print the package data for all packages with the given attribute.
    If an invalid input is entered, prints a warning and calls run_lookup() again.
    :param: snapshot: Hashtable - Copy of master_package_table at a point in time.
    """
    print('Please choose a type of input to lookup: \n'
          '    1. Package ID\n'
          '    2. Delivery Address\n'
          '    3. Delivery Deadline\n'
          '    4. Delivery City\n'
          '    5. Delivery Zip Code\n'
          '    6. Package Weight\n'
          '    7. Delivery Status\n'
          '    8. Return to Main Menu\n')
    user_input = input('Enter a number: ')

    if user_input == '1':
        try:
            key = int(input('    Please enter a Package ID: '))
            if snapshot.get(key):
                print('')
                snapshot.get(key).print_package()
                run_lookup(snapshot)
            else:
                print('\n --- No package found ---')
                run_lookup(snapshot)
        # If input throws ValueError print message
        except ValueError:
            print('\n        ValueError: Please try again with a correct value.\n')
            run_lookup(snapshot)

    # Lookup via delivery address. Can be a full or partial address.
    elif user_input == '2':
        val = input('    Please enter a full or partial delivery address: ')
        package_list = []
        for p in snapshot.get_values():
            # User can enter a cardinal or its abbreviation.
            if val.upper().replace(' SOUTH', ' S').replace(' WEST', ' W') \
                    .replace(' NORTH', 'N').replace(' EAST', ' E') \
                    in p.get_address():
                package_list.append(p)
        print_results(package_list, True)
        run_lookup(snapshot)

    # Lookup via delivery deadline.
    elif user_input == '3':
        val = input('    Please enter a delivery deadline: ')
        package_list = []
        for p in snapshot.get_values():
            # Allows partial strings. Eg. '30' will return any deadline containing '30' (10:30, 09:30)
            # %H or HH. Eg. 09:30 or 9:30 will return any deadline containing 09:30.
            # Note: While it works, AM and PM could probably be handled better.
            if val.upper() in p.get_deadline():
                package_list.append(p)
        print_results(package_list, True)
        run_lookup(snapshot)

    # Lookup via delivery city. Can be a full or partial city.
    elif user_input == '4':
        val = input('    Please enter a city: ')
        package_list = []
        for p in snapshot.get_values():
            if val.upper() in p.get_city():
                package_list.append(p)
        print_results(package_list, True)
        run_lookup(snapshot)

    # Lookup via zip code
    elif user_input == '5':
        val = input('    Please enter a delivery zip code: ')
        package_list = []
        for p in snapshot.get_values():
            if p.get_zip_code() == val:
                package_list.append(p)
        print_results(package_list, True)
        run_lookup(snapshot)

    # Lookup via package weight.
    elif user_input == '6':
        # Weight must be in the same format/measurement as given in the WGUPS Package File.
        val = input('    Please enter a package weight: ')
        package_list = []
        for p in snapshot.get_values():
            if p.get_weight() == val:
                package_list.append(p)
        print_results(package_list, True)
        run_lookup(snapshot)

    # Lookup via delivery status.
    elif user_input == '7':
        val = None
        checked = False
        # User enters the desired status to look up.
        # Invalid inputs will continue the while loop.
        while not checked:
            print('\n    Please choose a delivery status: \n'
                  '        1. AT HUB\n'
                  '        2. EN-ROUTE\n'
                  '        3. Delivered')
            val = input('\n    Enter a status number: ')
            if val == '1':
                val = 'AT HUB'
                checked = True
            elif val == '2':
                val = 'EN-ROUTE'
                checked = True
            elif val == '3':
                val = 'DELIVERED'
                checked = True
            else:
                print('\n        Invalid input. Please try again.')

        package_list = []
        for p in snapshot.get_values():
            if val.upper() in p.get_status().upper():
                package_list.append(p)
        print_results(package_list, True)
        run_lookup(snapshot)

    # Return to the main menu
    elif user_input == '8':
        main_menu()

    # Prints a warning and runs run_lookup() again.
    else:
        print('\n    Invalid input. Please try again\n')
        run_lookup(snapshot)


def run_simulation():
    """
    Runs the simulate_delivery_output() function to simulate the entire day's delivery operation.
    """
    print('\n------====== DELIVERY SIMULATION ======------\n')
    simulate_delivery_output()
    print('')
    main_menu()


def create_snapshot():
    """
    This function will create a 'snapshot' copy hashtable of all packages and their attributes in the
    master_package_table HashTable at a given time, for use with the run_lookup() function.
    :return: snapshot - Hashtable copy of master_package_table at a certain time.
    """
    # Initialize new snapshot Hashtable
    snapshot = Hashtable()
    # Get desired time for snapshot
    formatted_val_time = get_time_input()
    print('')
    val_time_str = datetime.datetime.strftime(formatted_val_time, '%H:%M')
    # Delivery must be simulated to lookup package status at times during the day.
    master_package_table = simulate_delivery()
    print('\nRetrieving snapshot of package table data from the specified time: [' + val_time_str + ']\n')
    for p in master_package_table.get_values():
        # Lookup the latest time stamp in each package's history that is on or before the user given time to map,
        # else map the default[0] datetime into the snapshot hashtable.
        latest_time_stamp = None
        for ts in p.get_history():
            if formatted_val_time >= ts:
                latest_time_stamp = p.get_history()[ts]
        if latest_time_stamp:
            snapshot.set(int(p.get_package_id()), latest_time_stamp)
        else:
            snapshot.set(int(p.get_package_id()), p.get_history[0])
    return snapshot


def snapshot_package_table():
    """
    This function will print a 'snapshot' hashtable of all packages and their attributes in the
    master_package_table HashTable at a given time.
    """
    print('\n------====== PACKAGE TABLE SNAPSHOT ======------')
    # Get desired time for snapshot
    formatted_val_time = get_time_input()
    print('')
    val_time_str = datetime.datetime.strftime(formatted_val_time, '%H:%M')
    # Delivery must be simulated to lookup package status at times during the day.
    master_package_table = simulate_delivery()
    print('\nRetrieving snapshot of package table data from the specified time: [' + val_time_str + ']\n')
    Package.print_package_horizontal_labels()
    for p in master_package_table.get_values():
        # Lookup the latest time stamp in each package's history that is on or before the user given time to print,
        # else prints the default[0] datetime.
        latest_time_stamp = None
        for ts in p.get_history():
            if formatted_val_time >= ts:
                latest_time_stamp = p.get_history()[ts]
        if latest_time_stamp:
            latest_time_stamp.print_package_horizontal()
        else:
            p.get_history[0].print_package_horizontal()

    sleep(0.26)
    main_menu()


def get_time_input():
    """
    Helper function that takes and validates a user input string for time an returns it in datetime format.
    :return: datetime of input string
    """
    val_time = None
    checked = False
    # Invalid inputs will be caught and continue the while loop.
    while not checked:
        try:
            val_time = datetime.datetime.strptime(
                input('\nPlease enter a time to check delivery status for in HH:MM format (example - \'8:35\' '
                      'or \'13:12\'): '), '%H:%M')
            checked = True
        except ValueError:
            print('\n    Invalid input. Please try again.')
    return datetime.datetime(t_date.year, t_date.month, t_date.day, val_time.hour, val_time.minute,
                             00)


def print_results(_list, horizontal):
    """
    Helper function to format and print a given list of results to the console.
    :param _list: A list of packages to
    format and print.
    :param horizontal: Boolean - If True, print package contents in horizontal line format. If
    False, print contents vertically
    """
    if len(_list) > 0:
        print('\n--- RESULTS ---\n')
        Package.print_package_horizontal_labels()
        for p in _list:
            if horizontal:
                p.print_package_horizontal()
            else:
                p.print_package()
        print('\n--- ' + str(len(_list)) + ' package(s) found ---\n')
    else:
        print("\n --- 0 package(s) found ---\n")
