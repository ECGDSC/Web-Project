from flask import Flask, render_template, jsonify, request
import sqlite3

app = Flask(__name__)

# Database initialization separated from connection function
def initialize_database():
    conn = sqlite3.connect("rooms.db")
    with open("roomsdb.sql") as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()

# Connection to the database
def get_db_connection():
    return sqlite3.connect("rooms.db")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/get/all", methods=["GET"])
def getAll():
    conn = get_db_connection()
    cursor = conn.cursor()
    all_status = cursor.execute("SELECT id, status FROM rooms").fetchall()
    all_status_list = [{"id": row[0], "status": row[1]} for row in all_status]
    conn.close()
    return jsonify(all_status_list)

@app.route("/api/get/<int:room_id>", methods=["GET"])
def get_status(room_id):
    conn = get_db_connection()
    try:
        status_row = conn.execute("SELECT status FROM rooms WHERE id = ?", (room_id,)).fetchone()
        if status_row:
            return jsonify({"id": room_id, "status": status_row[0]})
        else:
            return jsonify({"id": room_id, "status": "not found"}), 404
    finally:
        conn.close()

@app.route("/api/update/<int:room_id>", methods=["POST"])
def update_status(room_id):
    new_status = int(request.json['status'])
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE rooms SET status = ? WHERE id = ?", (new_status, room_id))
        conn.commit()
        if cursor.rowcount == 0:
            print(f"No rows were updated for room {room_id}. Check if room ID exists.")
        else:
            print(f"Room {room_id} updated to status {new_status}.")
        return jsonify({"success": True, "status": new_status})
    except Exception as e:
        conn.rollback()
        print(f"Error updating room {room_id}: {e}")
        return jsonify({"success": False, "error": str(e)}), 500
    finally:
        conn.close()

if __name__ == '__main__':
    app.run(debug=True, host="localhost")                        
