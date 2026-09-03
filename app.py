from flask import Flask

app = Flask(__name__)

# Vulnerabilidad intencional: contraseña quemada
MYSQL_PASSWORD = "super_secret_123"

@app.route("/")
def home():
    return "API Fase 2 con vulnerabilidad intencional"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)

