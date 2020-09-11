# Theo Perigo
# Student ID: 001083908
# C950 - Data Structures and Algorithms II
# NHP1 - Performance Assessment - WGUPS Routing Program
# 09/08/2020
# Hashtable.py


class Hashtable:
    """
    This class defines a custom implementation of a hashtable. A hashtable is a type of data structure used for fast
    mapping and searching for items in a list via a hashing algorithm. An item's key is hashed to find a bucket index
    to map its data to, and that key hash can later be used to search for an item, all at an average of O(1) time.
    This custom implementation uses chaining collision resolution, placing items with the same hash into the same
    bucket in order of mapping. This however potentially raises the time complexity to O(N). The hashtable has been
    coded to be easily modified for use with unknown keys and collision (via changing initial_size and using the
    default hash formula).
    """

    '''O(c)'''
    def __init__(self, initial_size=40):
        """
        Initializes the hashtable, creating a list 'h' of initial_size to be used as the hashtable's base.
        Also initializes lists for keys and values for quick retrieval
        """
        self.size = initial_size
        self.h = []
        for i in range(initial_size):
            self.h.append([])
        self.keys = []
        self.values = []

    '''O(1) - when __iter__ is called only iterates as one pass... I think...'''
    def __iter__(self):
        """
        Private helper function used to iterate through the hashtable
        """
        for x in self.h:
            yield x

    '''O(1)'''
    def _hash(self, key):
        """
        Function for hashing a key.
        For the WGUPS program where this hashtable will be implemented, all keys are known so we can avoid any collision
        and create a 'perfect hash' to insure O(1) time complexity for mapping and searching.
        :param key: int - The key to be hashed
        :return: int - hash value to be used as an index by the hashtable.
        """
        # Default Hash formula
        s = len(self.h)
        return key % s

        # Perfect hash (for WGUPS Package data). Use the default hash when size and keys are unknown.
        # Expects an int type (package_ID) as the key.
        # return key - 1

    '''O(1) - Worst is O(n) however the current hash guarantees O(1)'''
    def get(self, key):
        """
        This function searches the table and looks up the key. If found the key's value is returned. Else, return none.
        :param key: The key to search for and hashed.
        :return: value - The value associated with the found key
        :return: None - Returns None if the key is not found.
        """
        index = self._hash(key)
        bucket = self.h[index]
        if bucket:
            if len(bucket) == 1 and bucket[0][0] == key:
                return bucket[0][1]
            else:
                # Collision handling
                for i in range(len(bucket)):
                    if bucket[i][0] == key:
                        return bucket[i][1]
        return None

    '''O(1) - Worst is O(n) however the current hash guarantees O(1)'''
    def set(self, key, value):
        """
        This function maps a new (key, value) tuple item to an index in the hashtable determined by the key's hash
        value. If the indexed bucket is empty, simply append the new tuple to the bucket. If the key is already in the
        bucket, update the key with the new value. Else, append the new tuple to the end of the indexed bucket.
        The WGUPS program will use this to insert a (key, value) tuple of a (package.object.package_id, package.object).
        :param key: The key to be mapped and hashed.
        :param value: The value to be mapped.
        """
        index = self._hash(key)
        bucket = self.h[index]
        if len(bucket) == 0:
            bucket.append([key, value])
            self.keys.append(key)
            self.values.append(value)
        else:
            # Collision handling
            for i in range(len(bucket)):
                if bucket[i][0] == key:
                    bucket[i] = [key, value]
                    return
            bucket.append([key, value])
            self.keys.append(key)
            self.values.append(value)

    '''O(1) - Worst is O(n) however the current hash guarantees O(1)'''
    def remove(self, key):
        """
        This function removes the item with a matching key found at a the index in the hashtable determined by the
        key's hash value.
        :param key: The key to be hashed and removed (deleting the (key, value) tuple).
        :return: None - Returns None if key is not found.
        """
        index = self._hash(key)
        bucket = self.h[index]
        if bucket:
            if len(bucket) == 1 and bucket[0][0] == key:
                self.keys.remove(key)
                self.values.remove(self.get(key))
                self.h[index].clear()
            else:
                # Collision handling
                for i in range(len(bucket)):
                    if bucket[i][0] == key:
                        self.keys.remove(key)
                        self.values.remove(self.get(key))
                        del bucket[i]
                        return
        return None

    '''O(1)'''
    def get_keys(self):
        """
        This function returns a list of all the keys in the hashtable.
        :return: list - A list of all the keys in the hashtable.
        """
        # _list = []
        # for b in self.h:
        #     if len(b) == 1:
        #         _list.append(b[0][0])
        #     else:
        #         for i in range(len(b)):
        #             _list.append(b[i][0])
        # return sorted(_list)
        return self.keys

    '''O(1)'''
    def get_values(self):
        """
        This function returns a list of all the values in the hashtable.
        :return: list - A list of all the values in the hashtable.
        """
        # _list = []
        # for b in self.h:
        #     if len(b) == 1:
        #         _list.append(b[0][1])
        #     else:
        #         for i in range(len(b)):
        #             _list.append(b[i][1])
        # return _list
        return self.values

    '''O(n)'''
    def get_items(self):
        """
        This function returns all the items (key, value) pair tuples in the hashtable.
        :return: list - A list of all the items in the hashtable.
        """
        _list = []
        for b in self.h:
            for i in b:
                _list.append(i)
        return sorted(_list)

    '''O(1)'''
    def get_size(self):
        """
        This function returns the size of the hashtable.
        :return: int - The current size of the hashtable
        """
        return self.size
