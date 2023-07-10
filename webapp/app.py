import os
import psycopg2
from flask import Flask, render_template

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host="postgres",
                            database="sreality",
                            user="testuser",
                            password="testpassword",
                            port=5432)
    return conn


@app.route("/")
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM sreality_flats;")
    flats = list(cur.fetchall())
    cur.close()
    conn.close()
    return render_template("index_sreality.html", flats=flats)

if __name__ == "__main__":
    app.run(host=os.environ.get("BACKEND_HOST", "127.0.0.1"), port=8080)