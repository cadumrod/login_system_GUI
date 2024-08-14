import sqlite3

################################# FUNÇÕES BD #########################################


def db_conn(logsys_db):
    connection = sqlite3.connect(logsys_db)
    return connection


connection = db_conn("logsys.db")


def create_table(connection):
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   User TEXT NOT NULL,
                   Password TEXT NOT NULL
        )
    ''')
    connection.commit()


create_table(connection)
