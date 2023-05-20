import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def get_radius(self):
        return self.__radius
    
    def set_radius(self, value):
        if value < 0:
            self.__radius = 0
        else:    
            self.__radius = value

            

    radius =  property(get_radius, set_radius)   

def main():
    c = Circle(10)
    c.radius = 30
    print(c.radius)

if __name__ == '__main__':
    main()           