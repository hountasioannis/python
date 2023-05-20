def my_add(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b
    else:
        return 0
    
print(my_add(1,2))

print(my_add(1.5,2.5))

print(my_add("g","v"))