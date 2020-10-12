import sqlite3


all_members = []

def addUser(login, password):
    conn = sqlite3.connect('account_db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO main.Users (login, password, groups) VALUES(?, ?, 'Member')", (login, password))
    conn.commit()
    conn.close()

def getUserList ():
    all_members = []
    conn = sqlite3.connect('account_db')
    cursor = conn.cursor()
    for row in cursor.execute("SELECT DISTINCT * FROM main.Users WHERE groups = 'Member'"):
        all_members.append(row)
    conn.close()
    return all_members


