class Truck:
    def __init__(self, driver):
        self.MAX_PACKAGES = 16
        self.AVG_MPH = 18
        self.driver = driver
        self.on_truck = []
        self.status = 'STANDBY'
        self.distance_traveled = 0.0

    def load_package(self, p):
        if len(self.on_truck) < self.MAX_PACKAGES:
            self.on_truck.append(p)
            p.set_status('EN-ROUTE')
        else:
            print("ERROR: Truck is full. Number of packages loaded: ", len(self.on_truck))

    def deliver_package(self, p):
        self.on_truck.remove(p)
        p.set_status('DELIVERED')

    def unload_package(self, p):
        self.on_truck.remove(p)
        p.set_status('At Hub')

    def set_status(self, status):
        self.status = status
