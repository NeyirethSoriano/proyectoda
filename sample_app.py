import os
import pymysql
from flask import Flask

sample = Flask(__name__)

# Lectura segura desde variables de entorno
DB_HOST = os.getenv("DB_HOST", "db")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_NAME = os.getenv("DB_NAME", "adso_db_ejemplo")
FLASK_DEBUG = os.getenv("FLASK_DEBUG", "False").lower() in ("true", "1", "t")

@sample.route("/")
def home():
    try:
        conn = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            connect_timeout=3
        )
        conn.close()
        return "Conexion exitosa a la BD!"
    except Exception as e:
        return f"Error en la conexion: {e}"

if __name__ == "__main__":
    sample.run(host="0.0.0.0", port=5050, debug=FLASK_DEBUG)  # nosec B104
    