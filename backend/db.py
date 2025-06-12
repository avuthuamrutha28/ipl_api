import sqlite3
import json

conn = sqlite3.connect("players.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS players (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    amount INTEGER,
    country TEXT,
    role TEXT,
    team TEXT
)
''')

with open("players.json", "r") as f:
    data = json.load(f)

for player in data:
    cursor.execute('''
    INSERT INTO players (name, amount, country, role, team)
    VALUES (?, ?, ?, ?, ?)
    ''', (
        player['name'],
        player['amount'],
        player['country'],
        player['role'],
        player['team']
    ))

conn.commit()
conn.close()
