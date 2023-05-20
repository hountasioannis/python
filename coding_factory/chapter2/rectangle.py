a = int(input("give the length of a: "))
b = int(input("give the length of b: "))

if a > 0 and b > 0:
    if a == b:
        print("square")
    else:
        print("rectangle")

    print("square") if a == b else print ("rectangle")          