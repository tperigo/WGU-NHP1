# Hashtable class implementation
# Custom made for WGUPS
# All keys are known before hand. No collision.
# TODO - Eventually upgrade and set up buckets for collision
class Hashtable:
    # Initializes hashtable - creating a table 'h' of initial_size with each index set to None
    def __init__(self, initial_size=40):
        self.size = initial_size
        self.h = [None] * initial_size

    # Private Hash Function that takes an int key and returns a hash
    def _hash(self, key):
        # Hash formula of choice
        return key % len(self.h)

    # Set Function
    # Adds a value to the hashtable.
    def set(self, key, value):
        i = self._hash(key)
        self.h[i] = value

    # Get / Search Function.
    # Search for key. Return key if found, else return None
    def get(self, key):
        i = self._hash(key)
        if self.h[i]:
            return self.h[i]
        else:
            return None

    # Delete Function
    # Search for key, if found, remove from bucket.
    def remove(self, key):
        i = self._hash(key)
        self.h[i] = None

    # Returns the size of the hashtable
    def get_size(self):
        return self.size

    def __iter__(self):
        for x in self.h:
            yield x
