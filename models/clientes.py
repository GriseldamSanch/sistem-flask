#* clase cliente.
class Cliente:
    def __init__(self,nombre,email,telefono,password):
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.password = password
        self.historial_turnos = [] # para uso de administrador.

    # CREATE
    def nuevo_cliente(self,nombre,email,telefono,password):
        pass

    # DELETE:
    def eliminar_cliente(self):
        pass

    # cancelar turno
    def cancelar_turno(self):
        pass

  


