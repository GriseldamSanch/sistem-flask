# entrada a la aplicacion
import os
from datetime import datetime
from flask import Flask, flash, redirect, render_template, request, session, url_for
import config
from flask_mysqldb import MySQL #paquete conexion de  MYSQL
#seguridad de subida de archivos.
from werkzeug.utils import secure_filename

from models.clientes import Cliente
from models.profesionales import Profesional
from models.admin import Admin

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
@app.route('/login', methods=['GET','POST']) 
def login():
    if request.method == 'POST':
        # Procesar datos de login
        email = request.form['email']
        password = request.form['password']
        
        cur = mysql.connection.cursor() # Conexion a la base de datos
        cur.execute("SELECT * FROM clientes WHERE email = %s AND password = %s", (email, password))
        user = cur.fetchone() # Aqui se guarda la consulta
        cur.close() # Cerrar la base de datos
        
        if user is not None: # Si el usuario existe
            session["email"] = email
            session["password"] = password
            session["nombre"] = user[1]
            # Guardado de id del cliente que inicia sesion
            session["cliente_id"] = user[0]
            return redirect(url_for('getProfesionales')) # Redirige a la ruta turnos si coinciden los datos de la consulta
        else: 
            flash("Usuario o contraseña incorrectos", 'danger')
            return redirect(url_for('login')) # Redirige a la misma página para mostrar el mensaje de error
        
    return render_template('index.html') # Muestra el formulario de login para solicitudes GET
   
#TODO RUTA ADMIN LOGIN

@app.route('/admin_login', methods=['GET','POST']) 
def admin_login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        cur = mysql.connection.cursor()
        cur.execute("SELECT id, nombre, email, password FROM administradores WHERE email = %s", (email,))
        user = cur.fetchone()
        cur.close()
        
        if user and user[3] == password:  # Comparación directa de contraseña (inseguro para producción)
            session["email"] = email
            session["nombre"] = user[1]
            session["admin_id"] = user[0]
            flash(f"bienvenido {session['nombre']}", 'success')
            return redirect(url_for('getProfesionalesAdmin'))
        else: 
            flash("Usuario o contraseña incorrectos", 'danger')
            return redirect(url_for('admin_login'))
    else:
        return render_template('loginAdmin.html')
    
#TODO RUTA ADMIN PROFESIONALES
@app.route('/admin_profesionales', methods=['GET','POST'])
def getProfesionalesAdmin():
    #instancia de la clase profesionales
    profesionales = Profesional.get_profesionales(mysql) #! de clase profesionales
    # formulario eliminar profesional
    if request.method == 'POST':
        nombre = request.form['nombre']
        especialidad = request.form['especialidad']
        disponibilidad = request.form['disponibilidad']
        servicio_especial = request.form['servicio_especial']

        new_prof = Admin.agregar_profesional(mysql, nombre, especialidad, disponibilidad, servicio_especial)
        if new_prof:
            flash('Profesional agregado exitosamente.')
            return redirect(url_for('getProfesionalesAdmin'))
        else:
            flash('Error al agregar el profesional.')

    return render_template('getProfesionalesAdmin.html',profesionales=profesionales)


# TODO RUTA ADMIN ELIMINAR PROFESIONAL
@app.route('/eliminar_profesional', methods=['POST'])
def eliminar_profesional():
    if request.method == 'POST':
        profesional_id = request.form.get('profesional_id')
        delete = Admin.eliminar_profesional(mysql, profesional_id)
        if delete:
            flash('Profesional eliminado exitosamente', 'success')
        else:
            flash('Error al eliminar profesional', 'danger')
        return redirect(url_for('getProfesionalesAdmin'))
    


def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
        
        
        
# TODO RUTA VER PROFESIONALES 
@app.route('/profesionales', methods=['GET'])
def getProfesionales():
    #instancia de la clase profesionales
    profesionales = Profesional.get_profesionales(mysql) #! de clase profesional
    return render_template('getProfesionales.html',profesionales=profesionales)


#TODO  RUTA MOSTRAR DISPONIBILIDAD Y TURNOS POR PROFESIONAL
@app.route('/profesionales/<int:profesional_id>', methods=['GET','POST'])
def calendar_profesional(profesional_id):
    #*--update de horario_trabajo desde formulario------
    if request.method == 'POST':
        fecha = request.form['fecha']
        hora_inicio = request.form['hora']
        servicio = request.form['servicio']
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
        cliente_id = session.get('cliente_id') #! de clase Profesional
        #*----insercion de datos del formulario a la base de datos
        if Profesional.agregar_turno(mysql, profesional_id, fecha, hora_inicio, cliente_id, 1, 'reservado', servicio):
            flash('Turno reservado con éxito', 'success')
        else:
            flash('Hubo un error al reservar el turno', 'error')
        return redirect(url_for('calendar_profesional', profesional_id=profesional_id))

        #*--------------------------------------------------
    #*---- Obtén los turnos del profesional
    turnos = Profesional.obtener_turnos(mysql,profesional_id) #!de clase Profesional
    profName = Profesional.obtener_por_id(mysql,profesional_id).nombre #!de clase Profesional
    #*----------------------------------------
    #!-----------------------test
    mes = Profesional.mes_turnos(mysql,profesional_id)
    #*-----renderiza la plantilla calendarProf.html
    return render_template('calendarProf.html', profesional_id=profesional_id, mes=mes,profName=profName)


# TODO RUTA LOGOUT
@app.route('/logout')
def logout():
    session.clear() # cierra la sesion del usuario
    return redirect(url_for('home'))


# TODO RUTA NEW CLIENTE
@app.route('/new-cliente', methods=['GET', 'POST'])
def new_cliente():
    #* ------datos del formulario---------------------------------------
    if request.method == 'POST': # si se envia el formulario
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        telefono = request.form.get('telefono')
        password = request.form.get('password')
    #* -----------------------------------------------------------------
        if nombre and email and telefono and password: # si todos los campos estan completos
            #* Creacion de nuevo cliente
            nuevo_cliente = Cliente(nombre, email, telefono, password) #!de la clase Cliente
            #*------ insercion del nuevo cliente a la bd-----------
            if nuevo_cliente.nuevo_cliente(mysql,nombre,email,telefono,password):
                flash('Registro exitoso, inicia sesion', 'success')  # Añade el mensaje flash
                return redirect(url_for('new_cliente'))  # Redirige a la misma página para mostrar el mensaje
            #*-----------------------------------------------------
    return render_template('new-cliente.html')
    

# TODO NUEVA RUTA VER TURNOS Y CANCELAR TURNOS DE CLIENTE
@app.route('/cliente_turnos',methods=['GET', 'POST'])
def turnos_cliente():
    cliente_id = session.get("cliente_id")
    if request.method == 'POST':
        # Manejar la cancelación del turno
        turno_id = request.form.get('turno_id')
        if turno_id and cliente_id:
            try:
                cur = mysql.connection.cursor()
                cur.execute("DELETE FROM horarios_trabajo WHERE turno_id = %s AND cliente_id = %s", (turno_id, cliente_id))
                mysql.connection.commit()
                cur.close()
                print("turno cancelado")
                flash("Turno cancelado exitosamente.", "success")
            except Exception as e:
                print(f"Error al cancelar el turno: {e}")
                flash("Hubo un problema al cancelar el turno.", "danger")
        return redirect(url_for('turnos_cliente'))  # Redirigir para refrescar la lista de turnos
    # Manejar la obtención de turnos
    if cliente_id:
        turno_cliente = Cliente.get_turnos(mysql, cliente_id) 
    else:
        turno_cliente = []
    return render_template("turnos_cliente.html", turno_cliente=turno_cliente)













if __name__ == '__main__':
    app.run(debug=True)  # debug= true para que el servidor se reinicie cada vez que cambia el código.


