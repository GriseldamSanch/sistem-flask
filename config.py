import os # para cargar variables de entorno
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

# datos de conexion a la base de datos
MYSQL_HOST = os.getenv("MYSQL_HOST","")
MYSQL_USER = os.getenv("MYSQL_USER","")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD","")
MYSQL_DB = os.getenv("MYSQL_DB","")
HEX_SEC_KEY= os.getenv("HEX_SEC_KEY","12345")


