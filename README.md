#### sistema de Gestion de turnos para empresa de manicuria.

##### Desarrollo: Python

* Framework : Flask
* Data Base : MySQL
* Conexion DB : flask_mysqldb




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





dar estilo al template de los profesionales del admin.
reparar link del login del login admin.
reparar msj de bienvenido administrador




el administrador debe poder:
eliminar profesional  --- hecho---
agregar profesional   --hecho--


el profesional debe poder:  --no llego--
ver sus turnos diponibles.  --no llego--


el cliente debe poder:
reservar turno
cancelar turno
elegir metodo de pago

reparar el metodo del admi para incorporar especialidad_img y pueda cargar una imagen al nuevo profesional.



### 27/08
fix --> se agrega metodo nuevo_cliente() de clase Cliente en la ruta new_cliente().
fix --> se agrega clase Turno para gestionar y mostrar los turnos reservado del cliente.
fix ---> se agrega ruta turnos_clientes para mostrar los turnos reservados del cliente
fix --> se agrega en la ruta turnos_cliente para eliminar los turnos reservados del cliente.


- agregar en el nombre de sesion del cliente la ruta para ver y modificar en los templates que correspondan.
-ordenar en el folder static los archivos css.
- modular eliminar turnos desde la clase Cliente.
- agregar en el template para msj flash.
- mostrar en cada profesional " sin turnos reservados " cuando no tengan turnos reservados.
- eliminar de cada profesional o traer con algun fetch(si llego) una imagen aletoria.
- dar estilo a pagina de lista de profesionales de admin.
- muestra dos veces bienvenido admin, y se muestra debajo de la lista de profesionales.
- agregar medio de pagos de parte del cliente en reserva de turnos.
- reparar estilo del msj de registro exitoso de nuevo cliente y que redirecciones a la pagina de login (ruta)
- agregar texto selecciona un profesional en ruta profesionales.
- dar estilo a la ruta de visualizacion y cancelacion de turnos.
- agregar lista de precios



repaso:
ingreso al sistema con login ok
muestra de msj de error ok

registro de nuevo cliente ok
muestra de msj de registro exitoso ok (debe dar estilo)

seleccion de profesional para reserva de turno  ok
reserva de turno  ok
muestra de msj de reserva de turno ok
muestra de turnos reservados del mes del profesional ok
ingreso a la ruta cliente_turnos  ok
muestra de turnos reservados por el cliente ok
cancelacion turno ok
muestra de msj de cancelacion exitosa ok


medio de pago:  efectivo en local
