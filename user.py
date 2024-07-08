from connection import connection, Error


def user_menu():
    while True:
        print('''
        User Operations:
        1. Add a new user
        2. View user details
        3. Display all users
        ''')
        ans = input("How can we help ypu today?: ")
        
        if ans == "1":
            add_user()
        
        elif ans == "2":
            user_info()
        
        elif ans == "3":
            view_users()


def add_user():
    conn = connection()
    if conn is not None:
        try:
            cursor = conn.cursor()

            user_name = input("What is your name? ").title()
            email = input("What is your email? ")

            new_user = (user_name, email)
            query = "INSERT INTO users (name, email) VALUES (%s, %s)"

            cursor.execute(query, new_user)
            conn.commit() 
            print(f"New user {user_name} added successfully!")

        except Error as e:
            print(f"Error: {e}")
        
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close() 


def user_info():
    conn = connection()
    if conn is not None:

        try:    
            cursor = conn.cursor()

            target = input("Which user are you searching for?: ").title()

            query = "SELECT * FROM users WHERE name = %s"
            cursor.execute(query, (target,))

            for id, name, email in cursor.fetchall():
                print(f''' 
            - user id: {id}
            - name: {name}
            - email: {email}
            ''')


        except Error as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close() 


def view_users():
    conn = connection()
    if conn is not None:
        try:
            cursor = conn.cursor()

            query = "SELECT * FROM users;"
            cursor.execute(query)

            for id,name,email in cursor.fetchall():
                print(f"id#{id} - User: {name}, Email: {email}")
        
        except Error as e:
            print(f"Error: {e}")
        
        finally: 
            cursor.close()
            conn.close()

