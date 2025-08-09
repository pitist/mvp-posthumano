import sqlite3
from datetime import datetime

def guardar_prompt(prompt, respuesta):
    conn = sqlite3.connect('invocaciones.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS invocaciones (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        prompt TEXT,
        respuesta TEXT
    )''')
    c.execute('INSERT INTO invocaciones (timestamp, prompt, respuesta) VALUES (?, ?, ?)',
              (datetime.now().isoformat(), prompt, respuesta))
    conn.commit()
    conn.close()
