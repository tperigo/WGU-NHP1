# Theo Perigo
# Student ID: 001083908
# C950 - Data Structures and Algorithms II
# NHP1 - Performance Assessment - WGUPS Routing Program
# 09/08/2020
# ReadCSV.py

import csv
import datetime
from Hashtable import Hashtable
from Package import Package

# Assigns a variable for easy access to today's datetime
t_date = datetime.datetime.today()


def import_csv_package_file(filename):
    """
    Reads a CSV file of package data as input and parses the data into a HashTable of package objects.
    :param filename: A CSV for a package file to import and parse. Each 1 row x 7 columns is a unique package.
    :return: h: A HashTable containing the parsed package data.
    """
    # Initialize HashTable
    h = Hashtable()
    with open(filename) as csv_file:
        f = csv.reader(csv_file, delimiter=',')
        for row in f:
            # Creates a package object from data
            # Address cardinals are auto-replaced to their abbreviations.
            p = Package(row[0], row[1].upper()
                        .replace(' SOUTH', ' S').replace(' WEST', ' W').replace(' NORTH', ' N')
                        .replace(' EAST', ' E'), row[2].upper(), row[3].upper(), row[4], row[5], row[6], row[7])
            # Package timestamp is created at today's date:00:00:00.
            p.set_time_stamp(datetime.datetime(t_date.year, t_date.month, t_date.day, 00, 00, 00))
            # Inserts package into the HashTable, with the package ID as the key to be hashed, and the package object
            # paired as the value.
            h.set(int(p.get_package_id()), p)

        return h


# Reads a CSV file as input and parses the data into a list
def import_csv_distance_file(filename):
    """
    Reads a CSV file of a distance table  as input and parses the data into a list of locations and their distance
    weights to other locations in the list. Similar to a 2D array.
    :param filename: A CSV for a distance table file to import and parse. Each row is a unique location with their
    distance to itself (0) and to other locations.
    :return: distance_list: a list of all locations and their locations.
    """
    # Initialize list
    distance_list = []
    with open(filename) as csv_file:
        f = csv.reader(csv_file, delimiter=',')
        # Take each row from the file and append it to the list.
        for row in f:
            # Some string formatting
            row[0] = row[0].upper().lstrip(' ').replace('\n', ' ').replace('(', '').replace(')', '') \
                .replace(' SOUTH', ' S').replace(' WEST', ' W').replace(' NORTH', ' N').replace(' EAST', ' E')
            distance_list.append(row)
    return distance_list
