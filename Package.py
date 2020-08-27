# Class defining a Package object
class Package:
    def __init__(self, package_id, address, city, state, zip_code, deadline,
                 weight, notes):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.notes = notes

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

    def print_package(self):
        print('{} {}, {}, {}, {} - {} - {} - {}'.format(self.get_package_id(), self.get_address(), self.get_city(),
                                                        self.get_state(), self.get_zip_code(), self.get_deadline(),
                                                        self.get_weight(), self.get_notes()))
