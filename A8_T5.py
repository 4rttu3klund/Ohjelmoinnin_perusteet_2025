from A8_T5_lib import registerUser, authenticate

def showMainMenu() -> None:
    print("Options:")
    print("1 - Login")
    print("2 - Register")
    print("0 - Exit")

def showUserMenu() -> None:
    print("\nUser menu:")
    print("1 - View profile")
    print("2 - Change password")
    print("0 - Logout")

def main() -> None:
    print("Program starting.")
    while True:
        showMainMenu()
        choice = input("Your choice: ")
        if choice == "0":
            print("Exiting program.\n")
            break
        elif choice == "1":
            username = input("Insert username: ")
            password = input("Insert password: ")
            user = authenticate(username, password)
            if user is None:
                print("Authentication failed!\n")
            else:
                print("Authentication successful!\n")
                userMenu(user)
        elif choice == "2":
            username = input("Insert username: ")
            password = input("Insert password: ")
            registerUser(username, password)
            print("User registration completed!\n")
        else:
            print("Unknown option!\n")
    print("Program ending.")

def userMenu(user: tuple[int, str, str]) -> None:
    while True:
        showUserMenu()
        choice = input("Your choice: ")
        if choice == "0":
            print("Logging out...\n")
            break
        elif choice == "1":
            print(f"Profile ID {user[0]} - {user[1]}")
        elif choice == "2":
            print("Changing password not implemented.")
        else:
            print("Unknown option!")

if __name__ == "__main__":
    main()