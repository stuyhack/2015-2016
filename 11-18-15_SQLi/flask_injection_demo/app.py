from flask import Flask, render_template, request, redirect, url_for

import vulndb

app = Flask(__name__)

logged_in = False
username = ""

@app.route("/home")
@app.route("/home/")
def home():
    global logged_in
    global username
    if logged_in:
        page = "<p>oh my you logged in :O</p>\n<a href=\"/logout\">Logout</a>"
        page += "<p>%s</p>" % (username)
        return page
    else:
        return redirect(url_for("login"))

@app.route("/", methods=["GET", "POST"])
@app.route("/login", methods=["GET", "POST"])
@app.route("/login/", methods=["GET", "POST"])
def login():
    global logged_in
    global username
    if request.method == "GET":
        if logged_in:
            return redirect(url_for("home"))
        else:
            return render_template("login.html")
    else:
        assert(request.method == "POST")
        # This is where we check the user input
        if vulndb.is_valid_user(request.form['uname'], request.form['pword']):
            logged_in = True
            username = vulndb.get_user(request.form['uname']);
            return redirect(url_for("home"))
        else:
            logged_in = False
            return render_template("login.html")

@app.route("/logout")
def logout():
    global logged_in
    logged_in = False
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.debug = True
    app.run(host="127.0.0.1", port=8000)

