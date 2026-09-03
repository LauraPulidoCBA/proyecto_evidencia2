from flask import Flask
import os
import pymysql

app = Flask(__name__)

MYSQL_HOST = os.getenv("MYSQL_HOST", "servidor-bd")
MYSQL_USER = os.getenv("MYSQL_USER", "root")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE", "aprendices_db")

def get_connection():
    return pymysql.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE
    )

@app.route("/")
def home():
    return "API Fase 2 corregida y segura"

@app.route("/test-db")
def test_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT 1")
    result = cursor.fetchone()
    conn.close()
    return f"Resultado BD: {result}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
