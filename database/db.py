import sqlite3
import os

################################# FUNÇÕES BD #########################################


def db_conn(logsys_db):
    conn = sqlite3.connect(logsys_db)
    return conn


# Save .db file on database folder
current_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(current_dir, "logsys.db")


conn = db_conn(db_path)


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


def insert_user(conn, user, password):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Users (user,password) VALUES (?,?)", (user, password))
    conn.commit()
