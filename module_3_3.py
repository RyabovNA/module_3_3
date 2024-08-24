def print_params(a = 1, b = 'string', c = True):
    print(a, b, c)

print_params()
print_params(b = 5, a = 86)
print_params(a = 'Nikolay')
print_params(b = 25)
print_params(c = [1,2,3])


values_list = [78, False, "World"]
values_dict = {'a': "World", 'b': False, 'c': 78}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [True, 'Stanislav']
print_params(*values_list_2, 42)
