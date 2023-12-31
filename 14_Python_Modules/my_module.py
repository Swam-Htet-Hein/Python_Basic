def find_index(container, keyword):
    for index, name in enumerate(container):
        if keyword == name:
            return index
    pass

test = 'Testing'