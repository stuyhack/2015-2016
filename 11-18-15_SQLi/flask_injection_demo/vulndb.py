import sqlite3

def is_valid_user(uname, pword):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    QUERY = "SELECT * FROM users WHERE uname = \'%s\' AND pword = \'%s\'" % (uname, pword)
    print QUERY
    result = c.execute(QUERY).fetchall()
    conn.close()
    return len(result) == 1
