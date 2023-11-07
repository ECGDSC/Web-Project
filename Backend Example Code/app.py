import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

# initialize database
def initialize_database():
    connection = sqlite3.connect("user_database.db")
    with open("schema.sql") as f:
        connection.executescript(f.read())

    connection.commit()
    connection.close()

# opens a connection to the user_database.db database
def get_db_connection():
    # call the function that initializes the database
    initialize_database()
    conn = sqlite3.connect("user_database.db")
    conn.row_factory = sqlite3.Row
    return conn

# WEB ROUTES
# when accessing "https:~/" it should open the main frontend page of website
@app.route("/")
def index():
    conn = get_db_connection()
    # return the basis frontend page
    return render_template("index.html")

# API ROUTES
# when accessing "https:~/api/all" it will show raw data (which is not something you would see as a user!)
# define methods to be http GET request
@app.route("/api/all", methods=["GET"])
def getAll():
    conn = sqlite3.connect("user_database.db")
    cursor = conn.cursor()
    # using SQL query to retrieve desired information from database
    all_users = conn.execute("SELECT * FROM users").fetchall()
    return all_users

if __name__ == '__main__':
    app.run(debug=True,port=8000)
