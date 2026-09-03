from flask import Flask
import os

app = Flask(__name__)

# # Vulnerabilidad intencional: contraseña quemada
# MYSQL_PASSWORD = "super_secret_123"

# Corrección: usar variable de entorno en vez de contraseña quemada
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")

@app.route("/")
def home():
    return "API Fase 2 corregida y segura"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)

