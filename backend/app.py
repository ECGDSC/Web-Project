import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

# initialize database
def initialize_database():
    conn = sqlite3.connect("rooms.db")
    with open("roomsdb.sql") as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()

# opens a connection to the user_database.db database
def get_db_connection():
    initialize_database()
    conn = sqlite3.connect("rooms.db")
    return conn

# this is the root (landing page)
@app.route("/")
def index():
    return render_template("index.html")

# api route that accesses database to retreive all room status
@app.route("/api/all", methods=["GET"])
def getAll():
    conn = get_db_connection()
    cursor = conn.cursor()
    all_status = conn.execute("SELECT id, status FROM rooms").fetchall()
    return all_status

if __name__ == '__main__':
    app.run(debug=True, host="localhost")                        