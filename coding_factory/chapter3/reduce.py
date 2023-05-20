from functools import reduce

def main():
    my_ints = [1,2,3,4,5]

    result = reduce(lambda x, y: x * y, my_ints)

    print(result)

main()    