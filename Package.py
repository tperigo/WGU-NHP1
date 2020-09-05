# Class defining a Package object
import copy
import datetime

t_date = datetime.datetime.today()


class Package:
    def __init__(self, package_id, address, city, state, zip_code, deadline,
                 weight, notes, status='AT HUB'):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.status = status
        self.history = {}
        self.time_stamp = datetime.datetime(t_date.year, t_date.month, t_date.day, 00, 00, 00)

    def get_self(self):
        return self

    def get_package_id(self):
        return self.package_id

    def get_address(self):
        return self.address

    def get_city(self):
        return self.city

    def get_state(self):
        return self.state

    def get_zip_code(self):
        return self.zip_code

    def get_deadline(self):
        return self.deadline

    def get_weight(self):
        return self.weight

    def get_notes(self):
        if self.notes == '':
            self.notes = 'N/A'
        return self.notes

    def get_status(self):
        return self.status

    def get_time_stamp(self):
        return self.time_stamp

    def get_history(self):
        return self.history

    def set_package_id(self, package_id):
        self.package_id = package_id

    def set_address(self, address):
        self.address = address

    def set_city(self, city):
        self.city = city

    def set_state(self, state):
        self.state = state

    def set_zip_code(self, zip_code):
        self.zip_code = zip_code

    def set_deadline(self, deadline):
        self.deadline = deadline

    def set_weight(self, weight):
        self.weight = weight

    def set_notes(self, notes):
        self.notes = notes

    def set_status(self, status):
        self.status = status

    def set_time_stamp(self, time_stamp):
        self.time_stamp = time_stamp
        # time_str = self.time_stamp.strftime("%H:%M")
        self.history[time_stamp] = Package(self.package_id, self.address, self.city, self.state, self.zip_code, self.deadline, self.weight, self.notes, self.status)

    def print_package(self):
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
        print('    {}  |    {}, {}, {}, {}    |  {}  |  {} kg  |  {}  |  {} '.format(self.get_package_id(),
                                                                                     self.get_address(),
                                                                                     self.get_city(),
                                                                                     self.get_state(),
                                                                                     self.get_zip_code(),
                                                                                     self.get_deadline(),
                                                                                     self.get_weight(),
                                                                                     self.get_notes(),
                                                                                     self.get_status()))
