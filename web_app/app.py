from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

DB_FILE = r"C:\argus v\argus.db"

def get_logs():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM detection_logs ORDER BY id DESC")
    rows = cursor.fetchall()
    conn.close()
    return rows

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/logs")
def logs():
    data = get_logs()
    return render_template("logs.html", logs=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
