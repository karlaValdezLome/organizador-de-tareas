from flask import Flask, render_template, request, redirect, url_for
from flask_bcrypt import Bcrypt
app = Flask(__name__)

usuarios = {
    "admin": "karla",
    "usuario": "contraseña123"
}
bcrypt = Bcrypt(app)

@app.route('/iniciodesecion', methods=['GET', 'POST'])
def iniciodesecion():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        usuario_encontrado = usuarios.find_one({"usuario": username})

        if usuario_encontrado and bcrypt.check_password_hash(usuario_encontrado['password'], password):
            return redirect(url_for('index'))
        else:
            return render_template('iniciodesecion.html', error="Usuario o contraseña incorrectos")
            
    return render_template('iniciodesecion.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/recuperar_contraseña')
def recuperar_contraseña():
    return render_template('recuperar_contraseña.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':  
        user = request.form.get('usuario')
        password = request.form.get('password')
        if not user or not password:
            return render_template('registro.html', error="Datos incompletos")
        if usuarios.find_one({"usuario": user}):
            return render_template('registro.html', error="El usuario ya existe")

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        usuarios.insert_one({"usuario": user, "password": hashed_password})
        
        return redirect(url_for('iniciodesecion'))

if __name__ == '__main__':
    app.run(debug=True)