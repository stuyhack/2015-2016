from flask import Flask, render_template, request, session, redirect, url_for

import vulndb

app = Flask(__name__)

@app.route("/home")
@app.route("/home/")
def home():
    return "<p>oh my you logged in :O</p>"

@app.route("/", methods=["GET", "POST"])
@app.route("/login", methods=["GET", "POST"])
@app.route("/login/", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        if 'logged_in' in session and session['logged_in']:
            return redirect(url_for("home"))
        else:
            return render_template("login.html")
    else:
        assert(request.method == "POST")
        if vulndb.is_valid_user(request.form['uname'], request.form['pword']):
            session['logged_in'] = True
            return redirect(url_for("home"))
        else:
            session['logged_in'] = False
            return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.secret_key = "lmao this is #bestkey"
    app.debug = True
    app.run(host="127.0.0.1", port=8000)

