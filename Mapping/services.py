def data_mapper(key, value):
    res = {}
    counter = 0
    while counter < len(key):
        res[key[counter]] = value[counter]
        counter += 1

    return res