from book import book_menu
from user import user_menu

def main():
    while True:
        print(f'''
        Welcome to the Library Management System with Database Integration!
        ****
        Main Menu:
        1. Book Operations
        2. User Operations
        3. Quit
        ''')

        ans = input("How can we help you today?: ")

        if ans == "1":
            book_menu()
        elif ans == "2":
            user_menu()
        else:
            print("Thanks for using our database! -Bye!")
            break

main()