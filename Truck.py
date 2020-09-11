# Theo Perigo
# Student ID: 001083908
# C950 - Data Structures and Algorithms II
# NHP1 - Performance Assessment - WGUPS Routing Program
# 09/08/2020
# Truck.py

import datetime


class Truck:
    """
    This class defines a Truck object and the functions used to manipulate it. A Truck object represents a real world
    package delivery truck. A truck has an ID and can have one driver at a time. Trucks can hold a maximum of 16
    packages at once. These packages are placed in a list on_truck[]. Trucks move at a constant 18 MPH, and can keep
    track of their distance traveled in the variable_traveled.
    """

    '''O(1)'''
    def __init__(self, truck_id, driver, start_time):
        """
        Initialize the Truck object with the given parameters. MAX_PACKAGES and AVG_MPH are constants and should not
        be changed.
        :param truck_id: int - The truck ID number
        :param driver: string - The person assigned to drive the truck.
        :param start_time: datetime - The time that the Truck begins its route operation.
        """
        self.MAX_PACKAGES = 16
        self.AVG_MPH = 18
        self.truck_id = truck_id
        self.driver = driver
        self.on_truck = []
        self.status = 'STANDBY'
        self.distance_traveled = 0.0
        self.track_time = start_time

    '''O(1)'''
    def load_package(self, p):
        """
        This function loads a package onto the truck. It takes a Package object and if the number of packages in
        on_truck[] is less than MAX_PACKAGES, it then places the package object into the on_truck[] list,
        or else prints an error.
        :param p: A package object to load onto the Truck
        """
        if len(self.on_truck) < self.MAX_PACKAGES:
            self.on_truck.append(p)
            p.set_status('EN-ROUTE on Truck 0{}'.format(self.truck_id))
            p.set_time_stamp(self.track_time)
        else:
            print("ERROR: Truck is full. Number of packages loaded: ", len(self.on_truck))

    '''O(1)'''
    def deliver_package(self, p):
        """
        This function takes a package from the truck and delivers it to its destination. It takes a package object
        and removes it from the on_truck[] list. It then sets the package status to 'DELIVERED at (TIME)' and creates
        a new timestamp.
        :param p: A package object to deliver.
        """
        self.on_truck.remove(p)
        p.set_status('DELIVERED by ' + self.driver + ' at ' + self.track_time.strftime("%H:%M"))
        p.set_time_stamp(self.track_time)

    '''O(1)'''
    def unload_package(self, p):
        """
        This function unloads a package from the truck and returns it to the HUB. It takes a package object and
        removes it from the on_truck[] list. It then sets it status back to 'AT HUB'.
        :param p: A package object to
        remove and return to the hub.
        """
        self.on_truck.remove(p)
        p.set_status('AT HUB')

    '''O(1)'''
    def set_status(self, status):
        """
        This function sets the Trucks status to the given string.
        :param status: string - Status to set for the Truck
        """
        self.status = status

    '''O(1)'''
    def get_time(self):
        """
        This function returns the truck's track_time value.
        :return: self.track_time: datetime - The current time tracked by the truck.
        """
        return self.track_time

    '''O(n)'''
    def travel(self, distance):
        """
        This function calculates the distance traveled by the truck and the time it took to travel that distance. It
        takes a float type distance, and sums it with its current distance_traveled. Then it calculates the time_delta
        by dividing the distance by the speed (self.AVG_MPH = 18), and adds that time_delta to the current
        self.track_time. Each package also has its time stamp updated every stop the truck makes for tracking purposes.
        :param distance: float - The distance (in miles) for how much the truck just traveled.
        """
        self.distance_traveled += distance
        time_delta = datetime.timedelta(hours=(distance / self.AVG_MPH))
        self.track_time = self.track_time + time_delta
        for p in self.on_truck:
            p.set_time_stamp(self.track_time)
