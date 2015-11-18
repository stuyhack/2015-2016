import sqlite3

conn = sqlite3.connect("users.db")
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS users (uname text, pword text)")
conn.commit()
conn.close()

def addUser():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES ('bob', 'bob');")
    c.execute("INSERT INTO users VALUES ('charlie', 'brown');")
    conn.commit()
    conn.close()

