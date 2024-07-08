import mysql.connector
from mysql.connector import Error

db = "library"
user = "root"
password = "Potato828"
host = "localhost"

def connection():
    try:
        conn = mysql.connector.connect(
            database = db,
            user = user,
            password = password,
            host = host
        )

       
        if conn.is_connected():
            # print("Success!")
            return conn

     # if connection fails
    except Error as e:
        print(f"Error: {e}")
        return None

# connection() --- running successfully