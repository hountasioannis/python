import sys
import config
sys.path.append(config.APP_PATH)
from service import teacher_service

def menu():
    print("choose one of the following:")
    print("1 to insert a teacher ")
    print("2 to update a teacher ")
    print("3 to delete a teacher ")
    print("4 to find a teacher by lastname")
    print("5 to exit ")
    

def main():
    while True:
        menu()
        try:
            choice = int(input("choose one: "))
        

            if  choice == 1:
                firstname = input("enter firstname :")
                lastname = input("enter lastname:")
                print(teacher_service.TeacherServiceImpl.insert_teacher(firstname, lastname))
            elif choice == 2:
                id = int(input("enter id: "))
                firstname = input("enter firstname:")
                lastname = input("enter lastname:") 
                print(teacher_service.TeacherServiceImpl.update_teacher(id, firstname, lastname))
            elif choice == 3:
                id = int(input("enter id: "))
                print(teacher_service.TeacherServiceImpl.delete_teacher(id))
            elif choice == 4:
                lastname = input("enter lastname:")
                print(teacher_service.TeacherServiceImpl.get_teacher_by_lastname(lastname))
            elif choice == 5:
                break
            else:
                print("not valid choice")
        except ValueError:
            print("insert an integer")
            continue

    print("goodbye")


if __name__ == '__main__':
    main()    