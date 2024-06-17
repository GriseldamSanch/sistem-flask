#* clase cliente.
class Cliente:
    def __init__(self,nombre,email,telefono,password):
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.password = password
        self.historial_turnos = []

    def cancelar_turno(self, turno):
        # Lógica para cancelar turno
        pass
