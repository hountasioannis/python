def outer_func():
    print("outer func Started")

    def inner_func():
        print("inner func started")

    inner_func()

    print("outer ok")

def main():
    outer_func()

main()