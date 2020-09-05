from time import sleep


def UserInterface():
    intro()
    main_menu()


def intro():
    print('------====== WGUPS ver. 0.9.1 BETA ======------\n')


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
        run_wgups()
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

    elif user_input == '2':
        val = input('    Please enter a Delivery Address: ')
    elif user_input == '3':
        val = input('    Please enter a Delivery Deadline: ')
    elif user_input == '4':
        val = input('    Please enter a Delivery Zip Code: ')
    elif user_input == '5':
        val = input('    Please enter a Package Weight: ')
    elif user_input == '6':
        val = input('    Please enter a Delivery Status: ')
    elif user_input == '7':
        main_menu()
    else:
        print('    Invalid input. Please try again...')
        run_lookup()


def run_print_package_table():
    pass


def run_wgups():
    pass
