import sqlite3

def initiate_db(dbUser):
    with sqlite3.connect(dbUser) as connection:
        cursor = connection.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER NOT NULL,
        balance INTEGER NOT NULL);
        ''')
        connection.commit()

def add_user(dbUser, username, email, age):
    with sqlite3.connect(dbUser) as connection:
        cursor = connection.cursor()
        cursor.execute('''INSERT INTO Users (username, email, age, balance) VALUES(?, ?, ?, ?)''',
                       (f'{username}', f'{email}', f'{age}', 1000))

        connection.commit()

def is_included(dbUser, username):
    with sqlite3.connect(dbUser) as connection:
        cursor = connection.cursor()
        cursor.execute('''SELECT COUNT(*) FROM Users WHERE username=?''', (username,))
        count = cursor.fetchone()[0]
    return count > 0


if __name__ == '__main__':
    dbUser = 'database.db'
    initiate_db(dbUser)
    user_data = [
        ('dfcz', 'vasia@mail.ru', 25),
        ('vfif', 'masha@mail.ru', 33),
        ('uhbif', 'grisha@gmail.com', 46)
    ]

