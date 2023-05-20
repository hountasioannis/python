def welcome_guest():
    return "welcome guest"

def welcome_user(username):
    return f"welcome {username}"

def main():
    username: input("give username: ")

    message = welcome_user(username) if username else welcome_guest()

    print(message)

if __name__ == "__main__":
    main()    