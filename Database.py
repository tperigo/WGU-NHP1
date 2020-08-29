def print_package_table(t):
    for b in t:
        if b is not None:
            for i in b:
                i[1].print_package()
        else:
            print(None)
