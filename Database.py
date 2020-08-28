def print_package_table(t):
    for i in range(t.get_size()):
        if t.get(i) is not None:
            t.get(i).print_package()
        else:
            print(None)
