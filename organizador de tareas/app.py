from flask import Flask, render_template

app = Flask(__name__)


@app.route('/iniciodesecion')
def iniciodesecion():
    return render_template('iniciodesecion.html')


@app.route('/recuperar_contraseña')
def recuperar_contraseña():
    return render_template('recuperar_contraseña.html')


@app.route('/registro')
def registro():
    return render_template('registro.html')

if __name__ == '__main__':
    app.run(debug=True)