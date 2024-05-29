from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/inicio')
def inicio():
    return render_template('index.html')

@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')


@app.route('/productos')
def productos():
    return render_template('productos.html')

@app.route('/contactos')
def contactos():
    return render_template('contactos.html')

if __name__ == "__main__":
    app.run(debug=True, port=5000)

    
    
    
    