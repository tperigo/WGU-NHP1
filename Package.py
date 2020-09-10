# Theo Perigo
# Student ID: 001083908
# C950 - Data Structures and Algorithms II
# NHP1 - Performance Assessment - WGUPS Routing Program
# 09/08/2020
# Package.py

import datetime

# Assigns a variable for easy access to today's datetime
t_date = datetime.datetime.today()


class Package:
    """
    This class defines a Package object and the functions used to manipulate it. A package object represents a real
    world package to be delivered. A package has a ID, destination address, city, state, zip code, a deadline,
    a weight, special notes, and a status. A package also has a history dictionary that takes a timestamp as a key,
    and a copy of the packages attributes at that time. This tracks the changing statuses of the package as it moves
    throughout its delivery route.
    """

    def __init__(self, package_id, address, city, state, zip_code, deadline,
                 weight, notes, status='AT HUB'):
        """
        Initializes the package object with the given parameters.
        :param package_id:  int - The package's unique ID.
        :param address: string - The package's destination address.
        :param city:  string - The package's destination city.
        :param state:  string - The package's destination state.
        :param zip_code: string - The package's destination zip code.
        :param deadline: string - The package's delivery deadline.
        :param weight: string - The package's weight in kg.
        :param notes: string - Special notes about the package
        :param status: The package's current status.
        """
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.status = status
        # Initialize history dictionary
        self.history = {}
        # First timestamp for package object creation (default Today, 00:00:00)
        self.time_stamp = datetime.datetime(t_date.year, t_date.month, t_date.day, 00, 00, 00)

    def get_package_id(self):
        """
        :return: self.package_id - int
        """
        return self.package_id

    def get_address(self):
        """
        :return: self.address - string
        """
        return self.address

    def get_city(self):
        """
        :return: self.city - string
        """
        return self.city

    def get_state(self):
        """
        :return: self.state - string
        """
        return self.state

    def get_zip_code(self):
        """
        :return: self.zip_code - string
        """
        return self.zip_code

    def get_deadline(self):
        """
        :return: self.deadline - string
        """
        return self.deadline

    def get_weight(self):
        """
        :return: self.weight - string
        """
        return self.weight

    def get_notes(self):
        """
        :return: self.notes - string
        """
        if self.notes == '':
            # Formatting
            self.notes = 'N/A'
        return self.notes

    def get_status(self):
        """
        :return: self.status - string
        """
        return self.status

    def get_time_stamp(self):
        """
        :return: self.time_stamp - datetime
        """
        return self.time_stamp

    def get_history(self):
        """
        :return: self.history - dictionary
        """
        return self.history

    def set_package_id(self, package_id):
        """
        :param package_id: int
        """
        self.package_id = package_id

    def set_address(self, address):
        """
        :param address: string
        """
        self.address = address

    def set_city(self, city):
        """
        :param city: string
        """
        self.city = city

    def set_state(self, state):
        """
        :param state: string
        """
        self.state = state

    def set_zip_code(self, zip_code):
        """
        :param zip_code: string
        """
        self.zip_code = zip_code

    def set_deadline(self, deadline):
        """
        :param deadline: string
        """
        self.deadline = deadline

    def set_weight(self, weight):
        """
        :param weight: string
        """
        self.weight = weight

    def set_notes(self, notes):
        """
        :param notes: string
        """
        self.notes = notes

    def set_status(self, status):
        """
        :param status: string
        """
        self.status = status

    def set_time_stamp(self, time_stamp):
        """
        Takes a datetime timestamp during points of package activity (status changes) and adds the time_stamp to the
        dictionary as the key, with the value as as copy of the package's attributes at that time.
        This is my solution to package table status time-tracking (Rubric G1, G2, G3). Could be improved.
        :param time_stamp: datetime - Time of package activity
        """
        self.time_stamp = time_stamp
        self.history[time_stamp] = Package(self.package_id, self.address, self.city, self.state, self.zip_code,
                                           self.deadline, self.weight, self.notes, self.status)

    def print_package(self):
        """
        Prints out a vertically formatted package information for a single package to the console
        """
        print('Package ID: {}\n'
              'Address: {}\n'
              'City: {}\n'
              'State: {}\n'
              'Zip Code: {}\n'
              'Delivery Deadline: {}\n'
              'Package Weight {} kg\n'
              'Special Notes: {}\n'
              'Status: {}\n'.format(self.get_package_id(),
                                    self.get_address(),
                                    self.get_city(),
                                    self.get_state(),
                                    self.get_zip_code(),
                                    self.get_deadline(),
                                    self.get_weight(),
                                    self.get_notes(),
                                    self.get_status()))

    def print_package_horizontal(self):
        """
        Prints out a horizontally formatted package information for a single package to the console.
        """
        print('{:<3}| {:<40} | {:<18} | {:<6} | {:<8} | {:<9} | {:<6}  | {:<60}| {} '.format(self.get_package_id(),
                                                                                             self.get_address(),
                                                                                             self.get_city(),
                                                                                             self.get_state(),
                                                                                             self.get_zip_code(),
                                                                                             self.get_deadline(),
                                                                                             self.get_weight(),
                                                                                             self.get_notes(),
                                                                                             self.get_status()))

    @staticmethod
    def print_package_horizontal_labels():
        """
        Prints out a horizontally formatted labels to go with the print_package_horizontal() function.
        """
        print('{:<3}| {:<40} | {:<18} | {:<6} | {:<8} | {:<9} | {:<6}  | {:<60}| {} '.format('ID',
                                                                                             'Address',
                                                                                             'City',
                                                                                             'State',
                                                                                             'Zip Code',
                                                                                             'Deadline',
                                                                                             'Weight',
                                                                                             'Special Notes',
                                                                                             'Status'))
        print('------------------------------------------------------------------------------------------------------'
              '----------------------------------------------------------------------------------------------------')
