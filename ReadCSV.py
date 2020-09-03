import csv
from Hashtable import Hashtable
from Package import Package


# Reads a CSV file as input and parses the data into a hashtable of package objects.
def import_csv_package_file(filename):
    h = Hashtable()
    with open(filename) as csv_file:
        f = csv.reader(csv_file, delimiter=',')
        for row in f:
            p = Package(row[0], row[1].upper()
                        .replace(' SOUTH', ' S').replace(' WEST', ' W').replace(' NORTH', ' N')
                        .replace(' EAST', ' E'), row[2].upper(), row[3].upper(), row[4], row[5], row[6], row[7])
            h.set(int(p.get_package_id()), p)
        return h


# Reads a CSV file as input and parses the data into a list
def import_csv_distance_file(filename):
    distance_list = []
    with open(filename) as csv_file:
        f = csv.reader(csv_file, delimiter=',')
        for row in f:
            row[0] = row[0].upper().lstrip(' ').replace('\n', ' ').replace('(', '').replace(')', '')\
                .replace(' SOUTH', ' S').replace(' WEST', ' W').replace(' NORTH', ' N').replace(' EAST', ' E')
            distance_list.append(row)
    return distance_list
