import re

stack = []
num = 0

def push(list, item):
    list.append(item)

def pop(list):
    if list:
        return list.pop()
    else:
        print("stack is empty")

def print_menu():
    print("1.insert")
    print("2.get")
    print("q/Q quit")

def get_choice():
    return input("please select\n")   

def main():
    choice = 0
    num = 0
    out_num = 0

    while True:
        print_menu()
        choice = get_choice()

        if not choice:
            continue

        if choice == 'q' or choice == 'Q':
            break

        pattern = r"^\d+$"
        match = re.match(pattern, choice)

        if not match:
            print("Error in choice")
            continue

        choice = int(choice)

        match choice:
            case 1:
                num = input("insert a num")
                match = re.match(pattern, num)

                if not match:
                    print("Error in num")
                    continue

                num = int(num)
                push(stack, num)
                print(num, "pushed")

            case 2:
                out_num = pop(stack)
                print("you got:",out_num)

            case _:
                print("Not valid choice")

    print("goodbye")                    

if __name__ == '__main__':
    main()     
             