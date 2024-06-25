# clase profesionales
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
   def agregar_turno(mysql,profesional_id,fecha, hora_inicio,  cliente_id, reservado, estado,servicio):
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO horarios_trabajo (profesional_id,fecha, hora_inicio,  cliente_id, reservado, estado, servicio) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (profesional_id,fecha, hora_inicio,  cliente_id, reservado, estado, servicio))
        # Confirma la transacción
        mysql.connection.commit()
        # Cierra el cursor
        cur.close()

    
   
   
   
   
   


