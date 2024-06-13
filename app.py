# entrada a la aplcacion

from flask import Flask, render_template
app = Flask(__name__) # app instancia de Flask


@app.route('/', methods=['GET']) # ruta home
def home():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)  # debug= true para que el servidor se reinicie cada vez que cambia el código.

