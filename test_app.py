# test_app.py
from flask import Flask, request

app = Flask(__name__)

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    if username == "admin" and password == "password123":
        return "Login Successful"
    return "Login Failed"

app.run(debug=True)