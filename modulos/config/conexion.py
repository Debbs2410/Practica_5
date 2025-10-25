import mysql.connector
from mysql.connector import Error

def obtener_conexion():
    try:
        conexion = mysql.connector.connect(
            host='bcherte3ourwoiuadegi-mysql.services.clever-cloud.com',
            user='ubhpik0qmjf7ztsx',
            password='kmLa69jEQpi3F6asN1So',
            database='bcherte3ourwoiuadegi',
            port=3306
        )
        if conexion.is_connected():
            print("✅ Conexión establecida")
            return conexion
        else:
            print("❌ Conexión fallida (is_connected = False)")
            return None
    except mysql.connector.Error as e:
        print(f"❌ Error al conectar: {e}")
        return None
