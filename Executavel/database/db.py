import sqlite3
import os
import sys

################################# DB FUNCTIONS #########################################


# Determine the base directory for the database
def get_db_path():
    # Determine the base directory for the database
    if getattr(sys, 'frozen', False):
        # If running as an .exe
        base_dir = os.path.dirname(sys.executable)
    else:
        # If running as a python script
        base_dir = os.path.dirname(os.path.abspath(__file__))

    # Only add 'database' folder if it's not already part of the base_dir
    if not base_dir.endswith('database'):
        base_dir = os.path.join(base_dir, 'database')

    # Ensure the 'database' directory exists
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    # Define the full path to the database file
    db_path = os.path.join(base_dir, 'logsys.db')
    return db_path


# Db connection
def db_conn(db_path):
    conn = sqlite3.connect(db_path)
    return conn


# Path to database
db_path = get_db_path()

# Connection of database
conn = db_conn(db_path)


# Create table
def create_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   user TEXT NOT NULL,
                   password TEXT NOT NULL
        )
    ''')
    conn.commit()


create_table(conn)


# Insert user in db
def insert_user(conn, user, password):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Users (user,password) VALUES (?,?)", (user, password))
    conn.commit()


# Check if user already exists
def check_user_exists(conn, user):
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM users WHERE user = ?", (user,))
    return cursor.fetchone() is not None


# Check user password
def get_user_password(conn, user):
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE user = ?", (user,))
    result = cursor.fetchone()
    return result[0] if result else None
