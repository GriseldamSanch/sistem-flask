# entrada a la aplicacion
from datetime import datetime
from flask import Flask, flash, redirect, render_template, request, session, url_for
import config
from flask_mysqldb import MySQL #paquete conexion de  MYSQL

# from models.clientes import Cliente

from models.profesionales import Profesional

#--------------------------------------------------------------------------------------------------------------------------
#*                                        app y su conexion la DB                                          
#--------------------------------------------------------------------------------------------------------------------------

app = Flask(__name__) # app instancia de Flask
mysql = MySQL(app) #conexion de app a la base de datos

# configuracion de la app con los datos para la conexion
app.config["SECRET_KEY"] = config.HEX_SEC_KEY
app.config["MYSQL_HOST"] = config.MYSQL_HOST
app.config["MYSQL_USER"] = config.MYSQL_USER
app.config["MYSQL_PASSWORD"] = config.MYSQL_PASSWORD
app.config["MYSQL_DB"] = config.MYSQL_DB


#--------------------------------------------------------------------------------------------------------------------------
#*                                                  RUTAS
#--------------------------------------------------------------------------------------------------------------------------
""""
ruta home renderiza la plantilla index.html
"""
# todo   RUTA HOME
@app.route('/', methods=['GET']) 
def home():
    return render_template('index.html')


#TODO RUTA LOGIN
@app.route('/login', methods=['POST']) 
def login():
    # datos del formulario
    email = request.form['email']
    password = request.form['password']
    
    cur = mysql.connection.cursor() # conexion a la base de datos
    cur.execute("SELECT * FROM clientes WHERE email = %s AND password = %s", (email, password))
    user = cur.fetchone() # aqui se guarda la consulta
    print(user)
    cur.close() # cerrar la base de datos
    
    if user is not None: # si el usuario existe
        session["email"] = email
        session["password"] = password
        session["nombre"] = user[1]
        #!guardado de id del cliente que inica sesion
        session["cliente_id"] = user[0]
        
        return redirect(url_for('getProfesionales')) #si coinciden los datos de la consulta, redirige a la ruta turnos
    else: 
        return render_template('index.html',message="Usuario o contraseña incorrectos")
    

# TODO RUTA VER PROFESIONALES 
@app.route('/profesionales', methods=['GET'])
def getProfesionales():
    #instancia de la clase profesionales
    profesionales = Profesional.get_profesionales(mysql)
    return render_template('getProfesionales.html',profesionales=profesionales)

"""
TINYINT   ---> se utiliza en Myqsl para almacenar valores binarios y booleanos.
0: Representa FALSE.
1: Representa TRUE.
"""
#TODO  RUTA MOSTRAR DISPONIBILIDAD Y TURNOS POR PROFESIONAL
@app.route('/profesionales/<int:profesional_id>', methods=['GET','POST'])
def calendar_profesional(profesional_id):
    #*--update de horario_trabajo desde formulario------
    if request.method == 'POST':
        fecha = request.form['fecha']
        hora_inicio = request.form['hora']
    #*--------------------------------------------------

        #*--------validacion fecha----------------------

        

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM horarios_trabajo WHERE fecha = %s AND hora_inicio = %s", (fecha, hora_inicio))
        horario = cur.fetchone()
        cur.close()

        if horario is not None:
            flash('Ya existe un turno en esa fecha y hora','warning')
            return redirect(url_for('calendar_profesional', profesional_id=profesional_id))

        #*---------------------------------------------

        # ID del cliente desde la sesión
        cliente_id = session.get('cliente_id')

        #!----insercion de datos del formulario a la base de datos
        reservado = 1
        estado = 'reservado'
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO horarios_trabajo (profesional_id,fecha, hora_inicio,  cliente_id, reservado, estado) VALUES (%s, %s, %s, %s, %s, %s)",
                (profesional_id,fecha, hora_inicio,  cliente_id, reservado, estado))
        # Confirma la transacción
        mysql.connection.commit()
        # Cierra el cursor
        cur.close()
        # Redirigir después de insertar datos para evitar el reenvío del formulario
        return redirect(url_for('calendar_profesional', profesional_id=profesional_id))
        #!--------------------------------------------------
    
    #*---- Obtén los turnos del profesionals
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM horarios_trabajo WHERE profesional_id = %s", (profesional_id,))
    turnos = cur.fetchall()
   
    cur.close()
    #*----------------------------------------
    #*-----renderiza la plantilla calendarProf.html
    return render_template('calendarProf.html', profesional_id=profesional_id, turnos=turnos)


# TODO RUTA LOGOUT
@app.route('/logout')
def logout():
    session.clear() # cierra la sesion del usuario
    return redirect(url_for('home'))


# TODO RUTA NEW CLIENTE
@app.route('/new-cliente', methods=['GET', 'POST'])
def new_cliente():
    if request.method == 'POST': # si se envia el formulario
        nombre = request.form.get('nombre') # obtiene nombre del formulario
        email = request.form.get('email') # obtiene email del formulario
        telefono = request.form.get('telefono') # obtiene telefono del formulario
        password = request.form.get('password')# obtiene password del formulario
        if nombre and email and telefono and password: # si todos los campos estan completos
            cur = mysql.connection.cursor() #llamado la la base de datos
            cur.execute("INSERT INTO clientes (nombre, email, telefono, password) VALUES (%s, %s, %s, %s)", (nombre, email, telefono, password))#consulta sql
            mysql.connection.commit()# confirmacion del sql
            cur.close() #cierre 
            flash('Usuario registrado correctamente', 'success')  # Añade el mensaje flash
            return redirect(url_for('new_cliente'))  # Redirige a la misma página para mostrar el mensaje
    return render_template('new-cliente.html')
    
   








if __name__ == '__main__':
    app.run(debug=True)  # debug= true para que el servidor se reinicie cada vez que cambia el código.


