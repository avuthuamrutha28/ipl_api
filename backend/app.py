import os
print("📢 Actually running:", os.path.abspath(__file__))
from flask import Flask, jsonify
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def get_db_connection():
    conn = sqlite3.connect("players.db")
    conn.row_factory = sqlite3.Row
    return conn
@app.route("/")
def home():
    return "Welcome to ipl stats"

@app.route("/api/players", methods=["GET"])
def get_players():
    conn = get_db_connection()
    players = conn.execute("SELECT * FROM players").fetchall()
    conn.close()
    return jsonify([dict(player) for player in players])

if __name__ == "__main__":
    app.run(debug=True)

