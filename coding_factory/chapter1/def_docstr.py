def say_hello():
    """Prints hello coding factory"""
    print("hello coding factory")

def main():
    say_hello()
    print(say_hello.__doc__)
    help(say_hello)

main()    