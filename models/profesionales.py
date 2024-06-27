# clase profesionales
from datetime import date, datetime, timedelta


class Profesional:
   def __init__(self,id, nombre, especialidad, disponibilidad, servicio_especial, especialidad_img):
        self.id = id
        self.nombre = nombre
        self.especialidad = especialidad
        self.disponibilidad = disponibilidad
        self.servicio_especial = servicio_especial
        self.especialidad_img = especialidad_img

   @staticmethod
   def get_profesionales(myslq): #*obtener todos los profesionales
       cur = myslq.connection.cursor()#*cursor
       cur.execute("SELECT id, nombre, especialidad, disponibilidad, servicio_especial, especialidad_img FROM profesionales") # query
       profesionales_db = cur.fetchall()
       cur.close() #* cierre del cursor
       profesionales = [] #* lista de profesionales de la tabla
       for prof in profesionales_db:
           profesionales.append(Profesional(prof[0],prof[1],prof[2],prof[3],prof[4],prof[5]))
       return profesionales
   
   @staticmethod
   def obtener_por_id(mysql, profesional_id):#* obtener profesional por id
        cur = mysql.connection.cursor()
        cur.execute("SELECT id, nombre, especialidad, disponibilidad, servicio_especial, especialidad_img FROM profesionales WHERE id = %s", (profesional_id,))
        prof = cur.fetchone()
        cur.close()
        if prof:
            return Profesional(prof[0], prof[1], prof[2], prof[3], prof[4], prof[5])
        return None
   
   @staticmethod
   def obtener_turnos(mysql, profesional_id): # obtiene los turnos de un profesional
        cur = mysql.connection.cursor()
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM horarios_trabajo WHERE profesional_id = %s", (profesional_id,))
        turnos = cur.fetchall()
        cur.close()
        return turnos
   
   @staticmethod
   def agregar_turno(mysql,profesional_id,fecha, hora_inicio,  cliente_id, reservado, estado,servicio,metodo_pago):
           # Lógica para agregar el turno a la base de datos
    try:
        # Realiza la inserción en la base de datos
     cur = mysql.connection.cursor()
     cur.execute("INSERT INTO horarios_trabajo (profesional_id,fecha, hora_inicio,  cliente_id, reservado, estado, servicio,metodo_pago) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
     (profesional_id,fecha, hora_inicio,  cliente_id, reservado, estado, servicio,metodo_pago))
        # Confirma la transacción
     mysql.connection.commit()
        # Cierra el cursor
     cur.close()
     return True
    except Exception as e:
       return False

   @staticmethod
   def mes_turnos(mysql,profesional_id):
     today = date.today()
     first_day = today.replace(day=1)
     last_day = (today.replace(month=today.month % 12 + 1, day=1) -     timedelta(days=1))
     cur = mysql.connection.cursor()
     cur.execute("""
                 SELECT * FROM horarios_trabajo
                 WHERE profesional_id = %s AND fecha BETWEEN %s AND %s
                 ORDER BY fecha, hora_inicio
                 """, (profesional_id, first_day, last_day))
     turnos = cur.fetchall()
     cur.close()
     return turnos