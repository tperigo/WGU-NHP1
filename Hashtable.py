import csv
from Package import Package


# Node class for items
class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data

    def get_key(self):
        return self.key

    def get_data(self):
        return self.data

    def print_node(self):
        print('{} {}'.format(self.key, self.data))


# Hashtable class implementation
class Hashtable:
    # Initializes hashtable - creating a table 'h' of initial_size with each index set to None
    def __init__(self, initial_size=10):
        self.size = initial_size
        self.h = [None] * initial_size

    # Private Hash Function that takes an int key and returns a hash
    def _hash(self, key):
        # Hash formula of choice
        return key % len(self.h)

    # Set Function
    # Adds a Node(key/value pair) to the hashtable. If the hash-index is None, creates a new list at that index..
    # If the hash index location is occupied, uses chaining to resolve collision.
    # If if the key is already in the bucket, modifies the value. No duplicate keys allowed.
    def set(self, key, value):
        # Hash index
        i = self._hash(key)

        # Create new node holding the key value pair.
        n = Node(key, value)

        if self.h[i] is None:
            self.h[i] = [n]
        else:
            # Bucket
            b = self.h[i]

            # Search for key. If found, modify the value
            found = False
            for item in b:
                if item.get_key() == key:
                    item.data = value
                    found = True
                    break
            if not found:
                # Chaining
                b.append(n)

    # Get / Search Function.
    # Search for key. Return key if found, else return None
    def __getitem__(self, key):
        i = self._hash(key)
        b = self.h[i]

        for item in b:
            if item.get_key() == key:
                return item
        return None

    # Returns the size of the hashtable
    def get_size(self):
        return self.size

    # def __iter__(self):
    #    for x in self.h:
    #        yield x

    # Print a single buckets contents to the console
    def print_bucket(self, key):
        i = self._hash(key)
        b = self.h[i]
        if b is not None:
            for item in b:
                # print('[{}: {}]'.format(item.get_key(), item.get_data()), end=' ')
                item.get_data().print_package()
        else:
            print(None, end='')


def create_package_obj(read_csv):
    h = Hashtable()
    for row in read_csv:
        p = Package(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
        h.set(int(p.get_package_id()), p)
    return h


def import_csv_file(filename):
    with open(filename) as csv_file:
        read_csv = csv.reader(csv_file, delimiter=',')
        h = create_package_obj(read_csv)
    return h


def print_package_list(h):
    for i in range(h.get_size()):
        h.print_bucket(i)
        # Note: For formatting
