import os

from dotenv import load_dotenv
from peewee import PostgresqlDatabase

load_dotenv()

db = PostgresqlDatabase(
    os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT")
)

try:
    db.connect()
    print("Conexion realizada con exito")
    db.close()
except Exception as e:
    print(f"No se ha podido conectar a la base de datos.{e}")
