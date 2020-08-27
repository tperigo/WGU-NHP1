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

