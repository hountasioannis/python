def avg(*args):
    my_sum = 0
    for arg in args:
        my_sum += arg

    return my_sum / len(args)

def main():
    my_list = [10,20,30]
    print(avg(*my_list))

main()