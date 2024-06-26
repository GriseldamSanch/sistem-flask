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

##### 25/06
fix  ---> en login no se muestra el mjs de error usuario/contraseña incorrectos. se muestra el msj en la ruta profesionales/id   ✔
fix ---> al ingresar al sistema no deben estar login y register en el header. ✔
fix --> dar estilo a ruta profesionales. ✔
fix --> reparar links de redes sociales del footer.
fix --> reparar estilos en formulario de reserva de turnos. ✔
fix --> arreglar los archivos de estilo. 
fix --> arreglar msj de turno ya reservado en ruta profesionales/id ✔
fix --> agregar turno reservado con exito.se arreglo el metodo agregar.turno(). ✔
fix --> limitar hasta 1 mes la reserva de turno por profesional. se muestran los turnos reservados del mes actual. ✔
fix --> se muestra fecha en template en formato dia-mes-año ✔
fix --> agregar boton return profesionales ✔


que debe poder realizar el cliente:
* para ingresar al sistema el cliente debe estar registrado.
* para ingresar al sistema el cliente se debe logear
* se debe mostrar el nombre del cliente que inicia sesion en el sistema.
* el cliente podra elegir el profesional preferido y reservar un turno.
------------ falta-----
* el cliente debera PODER CANCELAR EL TURNO.
* el cliente debera PODER SELECCIONAR LA FORMA DE PAGO: EFECTIVO O TARJETA.   (agregar columna forma_pagos en horarios_laboral), si es a tarjeta mostrar un pequeño modal con formulario de pago por ese medio ficticio.?  agregar terminos y condiciones de reserva de turnos y pago.

----------------------falta
el profesional debera logearse de forma especial para ingresar al sistema.
podra ver sus turnos reservados y cambiarlos.
-----------------------falta
administrador:
debera poder ver historial de turnos los clientes y cancelar sus turnos.
debera poder ver y administrar a los profesionales (cambiar).
debera poder cambiar los turnos de los profesionales.
-------






