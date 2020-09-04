class Truck:
    def __init__(self, driver):
        self.MAX_PACKAGES = 16
        self.AVG_MPH = 18
        self.driver = driver
        self.on_truck = []

    def load_package(self, p):
        if len(self.on_truck) < self.MAX_PACKAGES:
            self.on_truck.append(p)
            p.set_status('En-route')

    def unload_package(self, p):
        self.on_truck.remove(p)
        p.set_status('Delivered')


# TODO - Greedy Package Algorithm + small route graph