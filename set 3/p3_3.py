def dictmap(dict, func):
    for key, val in dict.items():
        dict[key] = func(val)