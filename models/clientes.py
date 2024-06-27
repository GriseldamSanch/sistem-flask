from models.turnos import Turno

#* clase cliente.
class Cliente:
    def __init__(self,nombre,email,telefono,password):
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.password = password
        self.historial_turnos = [] # para uso de administrador.

#--------------------------------------------------------------------------------------------------------------------------
# *                                                  nuevo_cliente
# ?  agrega nuevo cliente en tabla Clientes
# @param name type  
# @param name type  
# @return Boolean
#--------------------------------------------------------------------------------------------------------------------------
    @classmethod 
    def nuevo_cliente(self,mysql,nombre,email,telefono,password):
        try:
            cur = mysql.connection.cursor() #llamado a la base de datos
            cur.execute("INSERT INTO clientes (nombre, email, telefono, password) VALUES (%s, %s, %s, %s)", (nombre, email, telefono, password))#consulta sql
            mysql.connection.commit()# confirmacion del sql
            # Obtener el ID del cliente recién insertado
            nuevo_cliente_id = cur.lastrowid
            cur.close() #cierre 
            return True
        except Exception as e:
            return False


    @classmethod
    def eliminar_cliente(self):
        pass


    @classmethod
    def cancelar_turno(self):
        pass


    @classmethod
    def get_turnos(cls, mysql, cliente_id):
        try:
            cur = mysql.connection.cursor()
            cur.execute("SELECT profesional_id, fecha, hora_inicio, servicio FROM horarios_trabajo WHERE cliente_id = %s", (cliente_id,))
            turnos_client = cur.fetchall()
            cur.close()
            
            turnos_cliente = [Turno(turno[0], turno[1], turno[2], turno[3]) for turno in turnos_client]
            return turnos_cliente
        except Exception as e:
            print(f"Error al obtener turnos: {e}")
            return [] #lista vacía en caso de error


        


  


