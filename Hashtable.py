# Hashtable class implementation
from Node import Node


def print_hashtable(h):
    for i in range(h.get_size()):
        h.print_bucket(i)


class Hashtable:
    # Initializes hashtable - creating a table 'h' of initial_size with each index set to None
    def __init__(self, initial_size=50):
        self.size = initial_size
        self.h = [None] * initial_size

    # Private Hash Function that takes an int key and returns a hash
    def _hash(self, key):
        # Hash formula of choice
        return key % len(self.h)

    # Set Function
    # Adds a Node(key/value pair) to the hashtable. If the hash-index is None, creates a new list at that index.
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
    def get(self, key):
        i = self._hash(key)
        b = self.h[i]

        for item in b:
            if item.get_key() == key:
                return item
        return None

    # Delete Function
    # Search for key, if found, remove from bucket.
    def remove(self, key):
        i = self._hash(key)
        b = self.h[i]

        if b is not None:
            for item in b:
                if item.get_key() == key:
                    b.remove(item)

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
        # Test formatting - Print None for empty buckets
        else:
            print(None)
