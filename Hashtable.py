# Hashtable class implementation
# Custom made for WGUPS


class Hashtable:
    # Initializes hashtable - creating a table 'h' of initial_size with each index set to None
    def __init__(self, initial_size=40):
        self.size = initial_size
        self.h = []
        for i in range(initial_size):
            self.h.append([])

    def __iter__(self):
        for x in self.h:
            yield x

    # Private Hash Function that takes an int key and returns a hash
    def _hash(self, key):
        # Hash formula of choice
        s = len(self.h)
        return key % s

    # Get / Look up Function.
    # Search for key. Return key's value if found, else return None
    def get(self, key):
        index = self._hash(key)
        bucket = self.h[index]
        if bucket:
            if len(bucket) == 1 and bucket[0][0] == key:
                return bucket[0][1]
            else:
                for i in range(len(bucket)):
                    if bucket[i][0] == key:
                        return bucket[i][1]
        return None

    # Set Function
    # Adds a value to the hashtable.
    def set(self, key, value):
        index = self._hash(key)
        bucket = self.h[index]
        if len(bucket) == 0:
            bucket.append([key, value])
        else:
            for i in range(len(bucket)):
                if bucket[i][0] == key:
                    bucket[i] = [key, value]
                    return
            bucket.append([key, value])

    # Search for key, if found, remove from bucket.
    def remove(self, key):
        index = self._hash(key)
        bucket = self.h[index]
        if bucket:
            if len(bucket) == 1 and bucket[0][0] == key:
                self.h[index].clear()
            else:
                for i in range(len(bucket)):
                    if bucket[i][0] == key:
                        del bucket[i]
                        return
        return None

    def get_keys(self):
        _list = []
        for b in self.h:
            if len(b) == 1:
                _list.append(b[0][0])
            else:
                for i in range(len(b)):
                    _list.append(b[i][0])
        return sorted(_list)

    def get_values(self):
        _list = []
        for b in self.h:
            if len(b) == 1:
                _list.append(b[0][1])
            else:
                for i in range(len(b)):
                    _list.append(b[i][1])
        return _list

    def get_items(self):
        _list = []
        for b in self.h:
            for i in b:
                _list.append(i)
        return sorted(_list)

    # Returns the size of the hashtable
    def get_size(self):
        return self.size
