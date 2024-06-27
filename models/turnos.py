#clase turno para obtener turnos
class Turno:
    def __init__(self,turno_id, profesional_id, fecha, hora_inicio, servicio):
        self.turno_id = turno_id
        self.profesional_id = profesional_id
        self.fecha = fecha
        self.hora_inicio = hora_inicio
        self.servicio = servicio
