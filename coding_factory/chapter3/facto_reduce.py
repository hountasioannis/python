from functools import reduce

def main():
    n = int(input("give an integer: "))
    result = reduce(lambda x, y: x * y, range(1, n + 1))
    print(result)

main()    