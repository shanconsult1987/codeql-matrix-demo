from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route("/user")
def user():

    id = request.args.get("id")

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE id=?"

    cursor.execute(query, (id,))

    return "User fetched"
