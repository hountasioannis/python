def join_args(separator, *args):
    return separator.join(args)

def main():
    sep = '-'

    days = ["Sunday", "Monday", "tuesday"]

    new_string = join_args(sep, *days)
    print(new_string)

main()    