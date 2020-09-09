# Theo Perigo
# Student ID: 001083908
# C950 - Data Structures and Algorithms II
# NHP1 - Performance Assessment - WGUPS Routing Program
# 09/08/2020
# UserInterface.py

import datetime
from time import sleep
from Routing import master_package_table, simulate_delivery, simulate_delivery_output

# Assigns a variable for easy access to today's datetime
t_date = datetime.datetime.today()


def UserInterface():
    """ Starts the WGUPS command line interface. Calls an intro() function, proceeded by the main_menu() function. """
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
          '    2. Simulate delivery\n'
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
        run_lookup()
    elif user_input == '2':
        run_simulation()
    elif user_input == '3':
        run_print_package_table()
    elif user_input == '4':
        run_exit()
    else:
        print('    Invalid input. Please try again...\n')
        main_menu()


def run_exit():
    """ Exits the program. """
    print('\n    Exiting program...')
    sleep(.5)
    exit()


def run_lookup():
    """
    Runs the package lookup function. This function takes a user input string to specify a type of package attribute
    to look up. The user then enters the desired package attribute and the program will search the
    master_package_table HashTable and print the package data for all packages with the given attribute. If an
    invalid input is entered, prints a warning and calls run_lookup() again.
    """
    print('\n------====== PACKAGE LOOKUP ======------\n')
    print('Please choose a type of input to lookup: \n'
          '    1. Package ID\n'
          '    2. Delivery Address\n'
          '    3. Delivery Deadline\n'
          '    4. Delivery Zip Code\n'
          '    5. Package Weight\n'
          '    6. Delivery Status\n'
          '    7. Return to Main Menu\n')
    user_input = input('Enter a number: ')

    if user_input == '1':
        key = int(input('    Please enter a Package ID: '))
        if master_package_table.get(key):
            print('')
            master_package_table.get(key).print_package()
            run_lookup()
        else:
            print('\n --- No package found ---')
            run_lookup()

    # Lookup via delivery address. Can be a full or partial address.
    elif user_input == '2':
        val = input('    Please enter a full or partial delivery address: ')
        package_list = []
        for p in master_package_table.get_values():
            # User can enter a cardinal or its abbreviation.
            if val.upper().replace(' SOUTH', ' S').replace(' WEST', ' W').replace(' NORTH', 'N').replace(' EAST', ' E') \
                    in p.get_address():
                package_list.append(p)
        print_results(package_list)

    # Lookup via delivery deadline.
    elif user_input == '3':
        val = input('    Please enter a delivery deadline: ')
        package_list = []
        for p in master_package_table.get_values():
            # Allows partial strings. Eg. '30' will return any deadline containing '30' (10:30, 09:30)
            # %H or HH. Eg. 09:30 or 9:30 will return any deadline containing 09:30.
            # Note: While it works, AM and PM could probably be handled better.
            if val.upper() in p.get_deadline():
                package_list.append(p)
        print_results(package_list)

    # Lookup via zip code
    elif user_input == '4':
        val = input('    Please enter a delivery zip code: ')
        package_list = []
        for p in master_package_table.get_values():
            if p.get_zip_code() == val:
                package_list.append(p)
        print_results(package_list)

    # Lookup via package weight.
    elif user_input == '5':
        # Weight must be in the same format/measurement as given in the WGUPS Package File.
        val = input('    Please enter a package weight: ')
        package_list = []
        for p in master_package_table.get_values():
            if p.get_weight() == val:
                package_list.append(p)
        print_results(package_list)

    # Lookup via delivery status.
    # This code will also allow for the user to input a desired time to lookup packages at that point
    # in time with the given delivery status.
    elif user_input == '6':
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

        formatted_val_time = get_time_input()

        print('')
        # Delivery must be simulated to lookup package status at times during the day.
        simulate_delivery()
        package_list = []
        for p in master_package_table.get_values():
            # Lookup the latest time stamp in each package's history that is on or before the user given time.
            latest_time_stamp = None
            for ts in p.get_history():
                if formatted_val_time >= ts:
                    latest_time_stamp = p.get_history()[ts]
            if latest_time_stamp:
                if val.upper() in latest_time_stamp.get_status().upper():
                    package_list.append(latest_time_stamp)
        print_results(package_list)

    # Return to the main menu
    elif user_input == '7':
        main_menu()

    # Prints a warning and runs run_lookup() again.
    else:
        print('\n    Invalid input. Please try again')
        run_lookup()


def run_simulation():
    """ Runs the simulate_delivery_output() function. This function will take the supplied package and distance files
    as input and utilize the the implemented program algorithms to simulate the day's delivery route and print the
    results to the console. """
    print('\n------====== DELIVERY SIMULATION ======------\n')
    simulate_delivery_output()
    print('')
    main_menu()


def run_print_package_table():
    """ This function will print out a 'snapshot' of all packages and their attributes in the master_package_table
    HashTable at a given time. """
    print('\n------====== PACKAGE TABLE ======------\n')
    formatted_val_time = get_time_input()
    print('')
    val_time_str = datetime.datetime.strftime(formatted_val_time, '%H:%M')
    # Delivery must be simulated to lookup package status at times during the day.
    simulate_delivery()
    print('')
    print('Retrieving snapshot of package table data from the specified time: [' + val_time_str + ']\n')
    for p in master_package_table.get_values():
        # Lookup the latest time stamp in each package's history that is on or before the user given time,
        # else prints the default datetime.
        latest_time_stamp = None
        for ts in p.get_history():
            if formatted_val_time >= ts:
                latest_time_stamp = p.get_history()[ts]
        if latest_time_stamp:
            latest_time_stamp.print_package_horizontal()
        else:
            p.get_history()[0].print_package_horizontal()
    print('')
    sleep(0.3)
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
                input('\n    Please enter a time to check delivery status for in HH:MM format (example - \'8:35\' '
                      'or \'13:12\'): '), '%H:%M')
            checked = True
        except ValueError:
            print('\n        Invalid input. Please try again.')
    return datetime.datetime(t_date.year, t_date.month, t_date.day, val_time.hour, val_time.minute,
                             00)


def print_results(_list):
    """
    Helper function to format and print a given list of results to the console.
    :param _list: A list of packages to format and print.
    """
    if len(_list) > 0:
        print('\n--- RESULTS ---\n')
        for p in _list:
            p.print_package()
        print('--- ' + str(len(_list)) + ' package(s) found ---')
        run_lookup()
    else:
        print("\n --- 0 package(s) found ---")
        run_lookup()
