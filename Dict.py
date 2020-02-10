my_dict = {'a':555, 'b':22222, 'c': 11,'d': 1, 'e': 222, 'f': 55}
keys = sorted(my_dict, key = my_dict.get, reverse = True)
print(keys)