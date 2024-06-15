# entrada a la aplicacion
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
        
        return redirect(url_for('getProfesionales')) #si coinciden los datos de la consulta, redirige a la ruta turnos
    else: 
        return render_template('index.html',message="Usuario o contraseña incorrectos")
    
# TODO RUTA VER PROFESIONALES 
@app.route('/profesionales', methods=['GET'])
def getProfesionales():
    #instancia de la clase profesionales
    profesionales = Profesional.get_profesionales(mysql)
    return render_template('getProfesionales.html',profesionales=profesionales)

#TODO  RUTA MOSTRAR CALENDARIO Y TURNOS DE UN PROFESIONAL

@app.route('/profesionales/<int:profesional_id>', methods=['GET'])
def calendar_profesional(profesional_id):
    profesional = Profesional.obtener_por_id(mysql,profesional_id) #obtiene el profesional por id
    turnos = Profesional.obtener_turnos(mysql,profesional_id) #obtiene los turnos del profesional
    return render_template('calendarProf.html', profesional=profesional, turnos=turnos)

#TODO   RUTA AGREGAR TURNO
@app.route('/profesionales/<int:profesional_id>/turnos', methods=['POST'])
def add_turno(profesional_id):
    #*verificar  que el usuario este logueado
    if not session.get('email'):
        flash('Debes iniciar sesion para reservar un turno')
        return redirect(url_for('login'))
    
    #*datos del formulario
    fecha = request.form.get('fecha')
    hora_inicio = request.form.get('horaInicio')
    hora_fin = request.form.get('horaFin')
    estado = request.form.get('estado')
    cliente_id = request.form.get('cliente_id')
    # Profesional.agregar_turno(mysql,profesional_id,fecha,hora_inicio,hora_fin,estado,cliente_id)
    # return redirect(url_for('calendar_profesional',profesional_id=profesional_id))

    #* verificar si el turno este disponible
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT id, estado FROM turnos
        WHERE profesional_id = %s AND fecha = %s AND hora_inicio = %s AND hora_fin = %s
    """, (profesional_id, fecha, hora_inicio, hora_fin))
    turno_existente = cur.fetchone()

    if turno_existente:
        if turno_existente[1] == 'reservado':
            flash("Este turno ya ha sido reservado por otra persona.", "error")
            cur.close()
            return redirect(url_for('calendar_profesional', profesional_id=profesional_id))
        else:
            # Actualizar el turno a reservado
            cur.execute("""
                UPDATE turnos
                SET estado = %s, cliente_id = %s
                WHERE id = %s
            """, ('reservado', cliente_id, turno_existente[0]))
    else:
        # Insertar un nuevo turno si no existe uno para ese horario
        cur.execute("""
            INSERT INTO turnos (profesional_id, fecha, hora_inicio, hora_fin, estado, cliente_id)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (profesional_id, fecha, hora_inicio, hora_fin, 'reservado', cliente_id))
    
    mysql.connection.commit()
    cur.close()

    flash("Turno reservado exitosamente.", "success")
    return redirect(url_for('calendar_profesional', profesional_id=profesional_id))





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

