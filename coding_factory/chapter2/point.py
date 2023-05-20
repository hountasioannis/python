class Point:
    __count = 0
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        Point.__count += 1

    def get_x(self):
        return self.__x    
    
    def get_y(self):
        return self.__y   
    
    def set_x(self, value):
         self.__x = value

    def set_y(self, value):
         self.__y = value


def main():
    p = Point(2, 3)

    p.set_x(10)
    p.set_y(20)
    print(p.get_x(), p.get_y())

if __name__ == '__main__':
    main()    