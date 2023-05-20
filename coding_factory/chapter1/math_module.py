import math as m

name = 'Alice'
age = 30

print('CF')
print("PI=", m.pi)
print("My name is", name, "and i am", age, "years old.")
print("My name is " + name + " and i am " + str(age) + " years old")

print("PI= %06.2f" %m.pi)
print("%s is %d years old" %(name, age))

print("Age is {0:2d}".format(age))
print("PI is {0:.3f}".format(m.pi))
print("{0} is {1} years old".format(name,age))
print("{0:*^10} {1:>20}".format(name,age))

print(f"My name is {name} and i am {age} years old!")
print(f"{name:>20}, {age:<5}")