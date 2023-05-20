def my_add(*args):
    result = 0
    for arg in args:
        result += arg
    return result

print(my_add())
print(my_add(10))
print(my_add(10, 20))