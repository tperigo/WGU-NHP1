import datetime


class Truck:
    def __init__(self, truck_id, driver, start_time):
        self.MAX_PACKAGES = 16
        self.AVG_MPH = 18
        self.truck_id = truck_id
        self.driver = driver
        self.on_truck = []
        self.status = 'STANDBY'
        self.distance_traveled = 0.0
        self.track_time = start_time

    def load_package(self, p):
        if len(self.on_truck) < self.MAX_PACKAGES:
            self.on_truck.append(p)
            p.set_status('EN-ROUTE')
            p.set_time_stamp(self.track_time)
        else:
            print("ERROR: Truck is full. Number of packages loaded: ", len(self.on_truck))

    def deliver_package(self, p):
        self.on_truck.remove(p)
        p.set_status('DELIVERED by ' + self.driver + ' at ' + self.track_time.strftime("%H:%M:%S"))
        p.set_time_stamp(self.track_time)

    def unload_package(self, p):
        self.on_truck.remove(p)
        p.set_status('AT HUB')

    def set_status(self, status):
        self.status = status

    def get_time(self):
        return self.track_time

    def travel(self, distance):
        self.distance_traveled += distance
        time_delta = datetime.timedelta(hours=(distance / self.AVG_MPH))
        self.track_time = self.track_time + time_delta
        for p in self.on_truck:
            p.set_time_stamp(self.track_time)
