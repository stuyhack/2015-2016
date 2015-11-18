import sqlite3

def is_valid_user(uname, pword):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    QUERY = "SELECT * FROM users WHERE uname = \'%s\' AND pword = \'%s\'" % (uname, pword)
    print QUERY
    result = []
    try:
        result = c.execute(QUERY).fetchall()
    except:
        return False
    conn.close()
    return len(result) == 1
