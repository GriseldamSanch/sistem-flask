#* clase cliente.
class Cliente:
    def __init__(self,nombre,email,telefono,password):
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.password = password
        self.historial_turnos = []
    def solicitar_turno(self, fecha, hora, profesional_preferido):
        # Lógica para solicitar turno
        pass
    
    def cancelar_turno(self, turno):
        # Lógica para cancelar turno
        pass
    
    def recibir_recordatorio(self, turno):
        # Lógica para recibir recordatorio
        pass