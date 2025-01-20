import sqlite3

from numpy.ma.core import product


def initiate_db(db_file):
    with sqlite3.connect(db_file) as connection:
        cursor = connection.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL, 
        description TEXT,
        price INT NOT NULL);
        ''')
        connection.commit()

def get_all_products(db_file):
    with sqlite3.connect(db_file) as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM Products')
        return cursor.fetchall()

if __name__ == '__main__':
    db_file = 'database.db'
    initiate_db(db_file)
    get_all_products(db_file)


