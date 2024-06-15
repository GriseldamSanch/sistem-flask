# clase profesionales
class Profesional:
   def __init__(self,id, nombre, especialidad, disponibilidad):
        self.id = id
        self.nombre = nombre
        self.especialidad = especialidad
        self.disponibilidad = disponibilidad

   @staticmethod    #????
   def get_profesionales(myslq): # obtener todos los profesionales
       cur = myslq.connection.cursor()#inicio de la consulta
       cur.execute("SELECT id, nombre, especialidad, disponibilidad FROM profesionales") # query
       profesionales_db = cur.fetchall() # guardamos la consulta
       cur.close() # cierre de la consulta
       profesionales = [] # aqui se guardaran los profesionales de la tabla
       for prof in profesionales_db:
           profesionales.append(Profesional(prof[0],prof[1],prof[2],prof[3])) #????
       return profesionales
   
   @staticmethod
   def obtener_por_id(mysql, profesional_id):# obtiener profesional por id
        cur = mysql.connection.cursor()
        cur.execute("SELECT id, nombre, especialidad, disponibilidad FROM profesionales WHERE id = %s", (profesional_id,))
        prof = cur.fetchone()
        cur.close()
        if prof:
            return Profesional(prof[0], prof[1], prof[2], prof[3])
        return None
   
   @staticmethod
   def obtener_turnos(mysql, profesional_id): # obtiene los turnos de un profesional
        cur = mysql.connection.cursor()
        cur.execute("SELECT id, fecha, hora_inicio, hora_fin, estado, cliente_id FROM turnos WHERE profesional_id = %s", (profesional_id,))
        turnos_db = cur.fetchall()
        cur.close()
        turnos = []
        for turno in turnos_db:
            turnos.append({
                'id': turno[0],
                'fecha': turno[1],
                'hora_inicio': turno[2],
                'hora_fin': turno[3],
                'estado': turno[4],
                'cliente_id': turno[5]
            })
        return turnos
   
   @staticmethod
   def agregar_turno(mysql, profesional_id, fecha, hora_inicio, hora_fin, estado, cliente_id):# agregar turno
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO turnos (profesional_id, fecha, hora_inicio, hora_fin, estado, cliente_id) VALUES (%s, %s, %s, %s, %s, %s)",
                    (profesional_id, fecha, hora_inicio, hora_fin, estado, cliente_id))
        mysql.connection.commit()
        cur.close()

    
   
   
   
   
   


