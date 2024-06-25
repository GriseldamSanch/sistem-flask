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


- el cliente debe poder cancelar el turno.
- se debe realizar la modularizacion del codigo utilizando las clases Profesional,Cliente y Administrador.


##### 23/06
se crea estilo para index.html
se crea estilo para getPorfesionales.html



####

crear nueva columna en tabla profesionales llamada imagen y colocar una imagen asociada a su especialidad.

falta estilo formulario de registro.
falta agregar clase administrador.
crear columna en horarios_trabajo con servicio a realizar
- error en la validacion de usuario ya registrado. template 
- no deslogearse al hacer click en login del header
- msj de ya existe turno existente agregar cierre darle estilo y que se muestre solo unos segundos







