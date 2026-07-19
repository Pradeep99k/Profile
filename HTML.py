from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary in-memory storage
users = {}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    username = request.form["username"]
    email = request.form["email"]
    password = request.form["password"]

    users[email] = {
        "username": username,
        "password": password
    }

    return redirect(url_for("home"))

@app.route("/login", methods=["POST"])
def login():
    email = request.form["email"]
    password = request.form["password"]

    if email in users and users[email]["password"] == password:
        return f"Welcome, {users[email]['username']}!"
    else:
        return "Invalid email or password."

if __name__ == "__main__":
    app.run(debug=True)
