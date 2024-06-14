# clase profesionales
class Profesional:
   def __init__(self,id, nombre, especialidad, disponibilidad):
        self.id = id
        self.nombre = nombre
        self.especialidad = especialidad
        self.disponibilidad = disponibilidad
   @staticmethod    #????
   def get_profesionales(myslq):
       cur = myslq.connection.cursor()#inicio de la consulta
       cur.execute("SELECT id, nombre, especialidad, disponibilidad FROM profesionales") # query
       profesionales_db = cur.fetchall() # guardamos la consulta
       cur.close() # cierre de la consulta
       
       profesionales = [] # aqui se guardaran los profesionales de la tabla
       
       for prof in profesionales_db:
           profesionales.append(Profesional(prof[0],prof[1],prof[2],prof[3])) #????
       return profesionales
       
          
   def actualizar_disponibilidad(self, nueva_disponibilidad):
        pass
