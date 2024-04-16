import sqlite3
from flask import Flask, render_template, jsonify, request

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
#Starthere (Make Post and Get route, something more effecient, something that only gets one room, rather than the whole three floors)
#api route that accesses databases to store/change a room status

@app.route("/api/all", methods=["POST"])

## https://stackoverflow.com/questions/51057966/flask-toggle-button-with-dynamic-label 
#@app.route("/api/all", methods=""
#https://github.com/scotty3785/pi_tv_remote/blob/master/templates/remote.html
## Think about how to update it periodically, if two people open on the same time and one of them checks a room, how would it immediately show to somebody else? 
#import other stuff flask 
# API route to get the status of a specific room

# API route to get the status of a specific room
@app.route("/api/room/<int:room_id>", methods=["GET"])
def get_room(room_id): 
    conn = get_db_connection()          # connect to db
    cursor = conn.cursor()              # Create a cursor, to exectue SQL commands
    cursor.execute("SELECT id, status FROM rooms WHERE id = ?", (room_id,))  # SQL command to fetch the room status by ID.
    room_status = cursor.fetchone()     # Fetch the first row of the results.
    conn.close()                        # Close connection.
    if room_status:
        return jsonify({'id': room_status[0], 'status': room_status[1]})  # convert the room status to JSON format and return it.
    else:
        return jsonify({'message': 'Room not found'}), 404  # Return a JSON response indicating room not found, 404.

# API route to update the status of a specific room
@app.route("/api/room/<int:room_id>", methods=["POST"])
def update_room(room_id):
    if 'status' in request.form:        # check if 'status' is provided in the form data of the request.
        new_status = request.form['status']  # retrieve the 'status' value from form.
        conn = get_db_connection()      # establish a db connection.
        cursor = conn.cursor()          # create cursor.
        cursor.execute("UPDATE rooms SET status = ? WHERE id = ?", (new_status, room_id))  # SQL command to update the room status.
        conn.commit()                   # Commit the change.
        conn.close()                    # close db connection.
        return jsonify({'message': 'Room status updated'})  # straightforward.
    else:
        return jsonify({'message': 'Invalid request'}), 400  # Return a JSON 400 error.
#def get one room or one floor
#db, dictionary
#def method to change state and update it 
#check if room is unavailable, if not, make it unavailable
#ask for password, use the same password for making it available


## Live update

if __name__ == '__main__':
    app.run(debug=True, host="localhost")                        