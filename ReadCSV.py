import csv
from Hashtable import Hashtable
from Package import Package


# Reads a CSV file as input and parses the data into a hashtable of package objects.
def import_csv_package_file(filename):
    h = Hashtable()
    with open(filename) as csv_file:
        f = csv.reader(csv_file, delimiter=',')
        for row in f:
            p = Package(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            h.set(int(p.get_package_id()), p)
        return h


# Reads a CSV file as input and parses the data into a list
def import_csv_distance_file(filename):
    distance_list = []
    with open(filename) as csv_file:
        f = csv.reader(csv_file, delimiter=',')
        for row in f:
            row[0] = row[0].lstrip(' ').replace('\n', ' - ')
            distance_list.append(row)
    return distance_list


# Converts the distance list to a dictionary.
def to_dictionary(_list):
    d = {}
    for row in _list:
        d[row[0]] = []
        iter_row = iter(row)
        next(iter_row)
        for value in iter_row:
            if value != '':
                d[row[0]].append(float(value))
    return d
