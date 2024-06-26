#clase administrador
"""
puede:
Agregar profesional
Eliminar profesional
Eliminar turno.
"""

class Admin:
    def __init__(self, nombre, email, password):
        self.nombre = nombre
        self.email = email
        self.password =  password   

    @classmethod
    def agregar_profesional(self):
        pass
    @classmethod
    def eliminar_turno(self):
        pass

    @classmethod
    def eliminar_profesional(self):
        pass
