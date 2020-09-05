import datetime
from time import sleep
from WGUPS import master_package_table, simulate_delivery, simulate_delivery_output

t_date = datetime.datetime.today()


def UserInterface():
    intro()
    main_menu()


def intro():
    print('\n------====== WGUPS CLI ver. 0.9.1 BETA ======------')


def main_menu():
    print('\n------====== MAIN MENU ======------\n')
    print("What would you like to do?")
    print('    1. Look up package(s)\n'
          '    2. Simulate delivery\n'
          '    3. View package table status at a specified time\n'
          '    4. Exit the program\n')
    user_input = input('Enter a number: ')
    return mm_options(user_input)


def mm_options(user_input):
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
    print('\n    Exiting program...')
    sleep(.5)
    exit()


def run_lookup():
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
        val = input('    Please enter a Package ID: ')
        for b in master_package_table:
            for i in b:
                if i[1].get_package_id() == val:
                    print('')
                    i[1].print_package()
                    return run_lookup()
        print('\n --- No package found ---')
        run_lookup()

    elif user_input == '2':
        val = input('    Please enter a full or partial delivery address: ')
        package_list = []
        for b in master_package_table:
            for i in b:
                if val.upper() \
                        .replace(' SOUTH', ' S') \
                        .replace(' WEST', ' W') \
                        .replace(' NORTH', 'N') \
                        .replace(' EAST', ' E') in i[1].get_address():
                    package_list.append(i[1])
        print_results(package_list)

    elif user_input == '3':
        val = input('    Please enter a delivery deadline: ')
        package_list = []
        for b in master_package_table:
            for i in b:
                if i[1].get_deadline() == val.upper():
                    package_list.append(i[1])
        print_results(package_list)

    elif user_input == '4':
        val = input('    Please enter a delivery zip code: ')
        package_list = []
        for b in master_package_table:
            for i in b:
                if i[1].get_zip_code() == val:
                    package_list.append(i[1])
        print_results(package_list)

    elif user_input == '5':
        val = input('    Please enter a package weight: ')
        package_list = []
        for b in master_package_table:
            for i in b:
                if i[1].get_weight() == val:
                    package_list.append(i[1])
        print_results(package_list)

    elif user_input == '6':
        val = None
        checked = False
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
        val_time = None
        checked = False
        while not checked:
            try:
                val_time = datetime.datetime.strptime(
                    input('\n    Please enter a time to check delivery status for in HH:MM format (example - \'8:35\' '
                          'or \'13:12\': '), '%H:%M')
                checked = True
            except ValueError:
                print('\n        Invalid input. Please try again.')
        formatted_val_time = datetime.datetime(t_date.year, t_date.month, t_date.day, val_time.hour, val_time.minute,
                                                00)
        print('')
        simulate_delivery()
        package_list = []
        for b in master_package_table:
            for i in b:
                latest_time_stamp = None
                for k in i[1].get_history():
                    if formatted_val_time >= k:
                        latest_time_stamp = i[1].get_history()[k]
                if latest_time_stamp:
                    if val.upper() in latest_time_stamp.get_status().upper():
                        package_list.append(latest_time_stamp)
        print_results(package_list)

    elif user_input == '7':
        main_menu()

    else:
        print('\n    Invalid input. Please try again')
        run_lookup()


def run_simulation():
    print('\n------====== DELIVERY SIMULATION ======------\n')
    simulate_delivery_output()
    print('')
    main_menu()


def run_print_package_table():
    print('\n------====== PACKAGE TABLE ======------\n')
    val_time = None
    try:
        val_time = datetime.datetime.strptime(
            input('    Please enter a time to check delivery status for in HH:MM format (example - \'8:35\' '
                  'or \'13:12\': '), '%H:%M')
    except ValueError:
        print('\n    Invalid input. Please try again')
        run_print_package_table()
    formatted_val_time = datetime.datetime(t_date.year, t_date.month, t_date.day, val_time.hour, val_time.minute, 00)
    val_time_str = datetime.datetime.strftime(formatted_val_time, '%H:%M')
    simulate_delivery()
    print('')
    print('Retrieving snapshot of package table data from the specified time: [' + val_time_str + ']\n')
    for b in master_package_table:
        for i in b:
            latest_time_stamp = None
            for k in i[1].get_history():
                if formatted_val_time >= k:
                    latest_time_stamp = i[1].get_history()[k]
            if latest_time_stamp:
                latest_time_stamp.print_package_horizontal()
            else:
                i[1].get_history()[
                    datetime.datetime(t_date.year, t_date.month, t_date.day, 00, 00, 00)].print_package_horizontal()

    print('')
    main_menu()


def print_results(_list):
    if len(_list) > 0:
        print('\n--- RESULTS ---\n')
        for p in _list:
            p.print_package()
        print('--- ' + str(len(_list)) + ' package(s) found ---')
        run_lookup()
    else:
        print("\n --- 0 package(s) found ---")
        run_lookup()
