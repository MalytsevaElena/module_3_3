def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(6)
print_params(6, 11, c=(12,32,16))
print_params(b=25)
print_params(c = [1,2,3])

values_list = [8, 'lalala', {4,5,6}]
values_dict = {"a": 729, "b": 'flip', "c": (10,9,8,7)}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [3.14,"str"]
print_params(*values_list_2, 42)
