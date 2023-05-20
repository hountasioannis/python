class Student:
    def __init__(self, id = 0 , firstname = '' , lastname = ''):
        self.__id = id
        self.__firstname = firstname
        self.__lastname = lastname
    
    @property
    def id(self):
        return self.__id
    
    @property
    def firstname(self):
        return self.__firstname
    
    @property
    def lastname(self):
        return self.__lastname
    
    @id.setter
    def id(self, value):
        self.__id = value

    @firstname.setter
    def firstname(self, value):
        self.__firstname = value

    @lastname.setter
    def lastname(self, value):
        self.__lastname = value


def main():
    st = Student()
    st.id = 1
    st.firstname = "Ioannis"
    st.lastname = "Chountas"
    print(st.id, st.firstname, st.lastname)

if __name__ == '__main__':
    main()        