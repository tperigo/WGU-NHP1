from time import sleep

from WGUPS import master_package_table, print_package_table, simulate_delivery


def UserInterface():
    intro()
    main_menu()


def intro():
    print('\n------====== WGUPS CLI ver. 0.9.1 BETA ======------\n')


def main_menu():
    print("What would you like to do?")
    print('    1. Look up package(s)\n'
          '    2. View full package table\n'
          '    3. Simulate delivery\n'
          '    4. Exit the program\n')
    user_input = input('Enter a number: ')
    return mm_options(user_input)


def mm_options(user_input):
    if user_input == '1':
        run_lookup()
    elif user_input == '2':
        run_print_package_table()
    elif user_input == '3':
        run_simulation()
    elif user_input == '4':
        run_exit()
    else:
        print('    Invalid input. Please try again...\n')
        main_menu()


def run_exit():
    print('    Exiting program...')
    sleep(.5)
    exit()


def run_lookup():
    print('\n------====== PACKAGE LOOKUP ======------\n')
    print('Please enter a type of input to lookup: \n'
          '    1. Package ID\n'
          '    2. Delivery Address\n'
          '    3. Delivery Deadline\n'
          '    4. Delivery Zip Code\n'
          '    5. Package Weight\n'
          '    6. Delivery Status\n'
          '    7. Return to Main Menu\n')
    user_input = input('Enter a number: ')

    if user_input == '1':
        val = input('    Please enter a Package ID: ')
        for b in master_package_table:
            for i in b:
                if i[1].get_package_id() == val:
                    print('')
                    i[1].print_package()
                    return run_lookup()
        print("        Package with specified ID not found.")
        run_lookup()

    elif user_input == '2':
        val = input('    Please enter a Delivery Address: ')
        package_list = []
        for b in master_package_table:
            for i in b:
                if val.upper() \
                        .replace(' SOUTH', ' S') \
                        .replace(' WEST', ' W') \
                        .replace(' NORTH', 'N') \
                        .replace(' EAST', ' E') in i[1].get_address():
                    package_list.append(i[1])

        if len(package_list) > 0:
            print('')
            for p in package_list:
                p.print_package()
            run_lookup()
        else:
            print("        Package with specified address not found.")
            run_lookup()

    elif user_input == '3':
        val = input('    Please enter a Delivery Deadline: ')
        package_list = []
        for b in master_package_table:
            for i in b:
                if i[1].get_deadline() == val.upper():
                    package_list.append(i[1])
        if len(package_list) > 0:
            print('')
            for p in package_list:
                p.print_package()
            run_lookup()
        else:
            print("        Package with specified deadline not found.")
            run_lookup()

    elif user_input == '4':
        val = input('    Please enter a Delivery Zip Code: ')
        package_list = []
        for b in master_package_table:
            for i in b:
                if i[1].get_zip_code() == val:
                    package_list.append(i[1])
        if len(package_list) > 0:
            print('')
            for p in package_list:
                p.print_package()
            run_lookup()
        else:
            print("        Package with specified zip code not found.")
            run_lookup()

    elif user_input == '5':
        val = input('    Please enter a Package Weight: ')
        package_list = []
        for b in master_package_table:
            for i in b:
                if i[1].get_weight() == val:
                    package_list.append(i[1])
        if len(package_list) > 0:
            print('')
            for p in package_list:
                p.print_package()
            run_lookup()
        else:
            print("        Package with specified weight not found.")
            run_lookup()

    elif user_input == '6':
        val = input('    Please enter a Delivery Status: ')
        package_list = []
        for b in master_package_table:
            for i in b:
                if i[1].get_status().upper() == val.upper():
                    package_list.append(i[1])
        if len(package_list) > 0:
            print('')
            for p in package_list:
                p.print_package()
            run_lookup()
        else:
            print("        Package with specified status not found.")
            run_lookup()
    elif user_input == '7':
        main_menu()
    else:
        print('    Invalid input. Please try again...')
        run_lookup()


def run_print_package_table():
    print('\n------====== PACKAGE TABLE ======------\n')
    print_package_table(master_package_table)
    print('')
    main_menu()


def run_simulation():
    print('\n------====== DELIVERY SIMULATION ======------\n')
    simulate_delivery()
    print('')
    main_menu()
