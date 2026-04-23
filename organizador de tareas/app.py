from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

usuarios = {
    "admin": "karla",
    "usuario": "contraseña123"
}

@app.route('/iniciodesecion', methods=['GET', 'POST'])
def iniciodesecion():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in usuarios and usuarios[username] == password:
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

@app.route('/registro')
def registro():
    return render_template('registro.html')

if __name__ == '__main__':
    app.run(debug=True)