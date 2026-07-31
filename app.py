from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "<h1>Hola, mi aplicación Flask funciona correctamente 🚀</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)