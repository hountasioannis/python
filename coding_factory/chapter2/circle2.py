import math

class Circle:
    __count = 0
    def __init__(self, radius):
        self.__radius = radius
        Circle.__count += 1

    @property
    def radius(self):
        return self.__radius
    
    @radius.setter
    def radius(self, value):
        if value < 0:
            self.__radius = 0
        else:    
            self.__radius = value

    @classmethod
    def count(cls):
        return cls.__count        

     

def main():
    c = Circle(10)
    c.radius = 30
    print(c.radius, Circle.count())

if __name__ == '__main__':
    main()           