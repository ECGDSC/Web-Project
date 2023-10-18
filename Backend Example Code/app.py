import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

# initialize database
def initialize_database():
    connection = sqlite3.connect("user_database.db")
    with open("schema.sql") as f:
        connection.executescript(f.read())

    # You can also create tables inside app.py
    # cursor.execute("""
    #     DROP TABLE IF EXISTS users

    #     CREATE TABLE users (
    #         id INTEGER PRIMARY KEY,
    #         name TEXT,
    #         email TEXT
    #     )
    # """)

    cur = connection.cursor()
    # initialize database by inserting few data
    cur.execute("INSERT INTO users (name, email) VALUES (?, ?)",
                ("Arata", "arata@earlham.edu")
                )
    cur.execute("INSERT INTO users (name, email) VALUES (?, ?)",
                ("Sharon", "sharon@earlham.edu")
                )
    cur.execute("INSERT INTO users (name, email) VALUES (?, ?)",
                ("Tien", "tien@earlham.com")
                )
    connection.commit()
    connection.close()

# opens a connection to the user_database.db database
def get_db_connection():
    initialize_database()
    conn = sqlite3.connect("user_database.db")
    conn.row_factory = sqlite3.Row
    return conn

# WEB ROUTES
@app.route("/")
def index():
    conn = get_db_connection()
    return render_template("index.html")

# API ROUTES
@app.route("/api/all", methods=["GET"])
def getAll():
    conn = sqlite3.connect("user_database.db")
    cursor = conn.cursor()
    all_users = conn.execute("SELECT * FROM users").fetchall()
    return all_users

if __name__ == "__main__":
    app.run(debug=True)