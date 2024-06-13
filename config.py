import os # para cargar variables de entorno
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

# datos de conexion a la base de datos
MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD","")
MYSQL_DB = os.getenv("MYSQL_DB","")


