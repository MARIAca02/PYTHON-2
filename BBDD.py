from flask import Flask, render_template, request
import mysql.connector

def create_app():
    app = Flask(__name__)

    # Conexión a la base de datos
    db = mysql.connector.connect(
        host="127.0.0.1",    # Dirección del servidor de la base de datos
        user="root",      # Nombre de usuario de la base de datos
        passwd="", # Contraseña de la base de datos
        database="python_bbdd" # Nombre de la base de datos
    )

    @app.route('/')
    def index():
        return render_template('exitoso.html')  # Renderiza el formulario HTML

    @app.route('/guardar_datos', methods=['POST'])
    def guardar_datos():
        cursor = db.cursor()
        nombre = request.form['nombre']
        tipo_documento = request.form['tipo_documento']
        numero_telefono = request.form['numero_telefono']
        email = request.form['email']
        contrasena = request.form['contrasena']
        
        cursor.execute("INSERT INTO usuarios (nombre, tipo_documento, numero_telefono, email, contrasena) VALUES (%s, %s, %s, %s, %s)", (nombre, tipo_documento, numero_telefono, email, contrasena))  # Inserta los datos en la base de datos
        db.commit()  # Confirma la transacción
        cursor.close()  # Cierra el cursor
        return 'Datos guardados correctamente'  # Retorna un mensaje de éxito

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

