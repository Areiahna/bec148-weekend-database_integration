from connection import connection, Error

def book_menu():
    while True:
        print('''
        Book Operations:
        1. Add a new book 
        2. Borrow a book 
        3. Return a book
        4. Search for a book
        5. Display all books
        ''')
        ans = input("How can we help you today?: ")

        if ans == "1":
            add_book()
        elif ans == "2":
            borrow_book()
        elif ans == "3":
            return_book()
        elif ans == "4":
            search()
        elif ans == "5":
            display_books()

def add_book():
    conn =  connection()
    if conn is not None:
        
        try: 
            cursor = conn.cursor()

            title = input("Enter book title: ").title()
            new_book = (title)

            query = "INSERT INTO books (title) VALUES %s"
            cursor.execute(query)
            conn.commit()

            print(f"New book {title} added successfully!")
        
        except Error as e:
            print(f"Error: {e}")

        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()


def borrow_book():  
    conn = connection()
    if conn is not None:

        try:
            cursor = conn.cursor()

            book = input("Which book would you like to borrow?: ").title()

            query = "SELECT * FROM books WHERE title = %s"
            cursor.execute(query,(book,))


            for id, title, availability in cursor.fetchall():
                if availability == 1:
                    print("This book is available")
                else:
                    print("This book is not available")
                

        except Error as e:
            print(f"Error: {e}")

        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()


def return_book():
    pass

def search():
    conn = connection()
    if conn is not None:

        try:
            cursor = conn.cursor()
            target = input("Which book are you looking for?: ").title()

            query = "SELECT * FROM books WHERE title = %s"

            cursor.execute(query,(target,))

            for id, title, availability in cursor.fetchall():
                if availability == 1:   
                    print(f"id#{id} - Title: {title}, Availability: True")
                else:
                    print(f"id#{id} - Title: {title}, Availability: False")
        
        except Error as e:
            print("Error : {e}")
        
        finally:
            if conn and conn.is_connected():
                conn.close()
                cursor.close()



def display_books():
    conn = connection()
    if conn and conn.is_connected():
        try:
            cursor = conn.cursor()

            query = "SELECT * FROM books;"
            cursor.execute(query)

            for id, title, availability in cursor.fetchall():
                if availability == 1:
                    print(f"id#{id} - Title: {title}, Availability: True")
                else:
                    print(f"id#{id} - Title: {title}, Availability: False")

        except Error as e:
            print(f"Error: {e}")

        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()
