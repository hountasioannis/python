def main():
    ch = input("give char: ")

    while True:
        print(ch, ord(ch))
        ch = input("give char: ")
        if ch == "#": break

    print("goodbye")

main()        