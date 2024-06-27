#clase administrador
"""
puede:
Agregar profesional
Eliminar profesional
Eliminar turno.
"""

class Admin:
    def __init__(self, nombre, email, password):
        self.nombre = nombre
        self.email = email
        self.password =  password   

    @classmethod
    def agregar_profesional(cls, mysql, nombre, especialidad, disponibilidad, servicio_especial, especialidad_img):
        try:
            cur = mysql.connection.cursor()
            cur.execute("""
                INSERT INTO profesionales (nombre, especialidad, disponibilidad, servicio_especial,especialidad_img) 
                VALUES (%s, %s, %s, %s, %s)
            """, (nombre, especialidad, disponibilidad, servicio_especial, especialidad_img))
            mysql.connection.commit()
            cur.close()
            return True
        except Exception as e:
            print(f"Error al agregar profesional: {e}")
            return False


    @classmethod
    def eliminar_turno(self):
        pass

    @classmethod
    def eliminar_profesional(cls,mysql,profesional_id): #elimina profesional
        try:
            cur = mysql.connection.cursor()
            # Ejecutar la consulta de eliminación
            cur.execute("DELETE FROM profesionales WHERE id = %s", (profesional_id,))
            mysql.connection.commit()
            cur.close()
            return True
        except Exception as e:
            print(f"Error al eliminar profesional: {e}")
            return False
 
