def main():
    ch = input("give char: ")

    while ch != "#":
        print(ch, ord(ch))
        ch = input("give char: ")

    print("goodbye")

main()        