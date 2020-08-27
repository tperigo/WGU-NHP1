import csv
from Hashtable import Hashtable
from Package import Package


# Reads a CSV file as input and parses the data into a hashtable of package objects.
def import_csv_file(filename):
    with open(filename) as csv_file:
        f = csv.reader(csv_file, delimiter=',')
        h = Hashtable()
        for row in f:
            p = Package(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            h.set(int(p.get_package_id()), p)
        return h
