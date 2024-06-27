#clase turno para obtener turnos
class Turno:
    def __init__(self, profesional_id, fecha, hora_inicio, servicio):
        self.profesional_id = profesional_id
        self.fecha = fecha
        self.hora_inicio = hora_inicio
        self.servicio = servicio
