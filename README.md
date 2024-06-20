#### sistema de Gestion de turnos para empresa de manicuria.

##### Desarrollo: Python

* Framework : Flask
* Data Base : MySQL


##### 19/06
modificacion de la tabla horarios_trabajo
se modifica la ruta calendar_profesional(profesional_id):
1. se crea de cero la logica para insersion para el update de la tabla horarios_trabajo
2. fix el envio del formulario al recargar la pagina. linea 85
3. se utiliza session para guardar el id del cliente y utilizarlo en calendar_profesional.

- se debe validar las fechas de los turnos de los profesionales.
- se debe limitar los horarios de los turnos segun cada profesional. hecho.
- el cliente debe poder cancelar el turno.
- se debe realizar la modularizacion del codigo utilizando las clases Profesional,Cliente y Administrador.





