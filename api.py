from flask import Flask, render_template, request, redirect, url_for
import os

api = Flask(__name__)
servidores = [{'nombre': 'Servidor de Jose', 'descripcion': 'Un lugar genial para hablar de videojuegos , anime y series en general'}, {'nombre': 'Servidor de Juan', 'descripcion': 'Aqui no se habla de nada por que no tengo servidor'}]
@api.route('/', methods=['GET', 'POST'])
def home():
    nombre = os.environ.get('VARIABLE_PRUEBA')
    mensajeindex = f'Hola mundo desde Flask, mi nombre es {nombre}'
    return render_template('index.html', servidores=servidores)

@api.route('/agregarservidor', methods=['POST'])
def agregar():
    servidores.append({'nombre': request.form.get('nombreservidor'), 'descripcion': request.form.get('descripcionservidor')})
    return redirect(url_for('home'))