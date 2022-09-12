from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.usuario import Usuario

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def todos():
    return render_template('todos_los_usuarios.html',usuarios=Usuario.get_all())

@app.route('/users/new')
def nuevo():
    return render_template('agrega_usuario.html')

@app.route('/user/create', methods=['POST'])
def agregar():
    Usuario.agregar (request.form)
    return redirect('/users')

@app.route('/users/mostrar/<int:id>')
def mostrar(id):
    data={
        "id":id
    }
    return render_template('mostrar.html',usuarios=Usuario.get_one(data))

@app.route('/users/actualizar', methods=['POST'])
def actualizar():
    Usuario.actualizar(request.form)
    return redirect('/users')

@app.route('/users/editar/<int:id>')
def editar(id):
    data={
        "id":id
    }
    return render_template('editar.html',usuarios=Usuario.get_one(data))

@app.route('/users/eliminar/<int:id>')
def eliminar(id):
    data={
        "id":id
    }
    Usuario.eliminar(data)
    return redirect('/users')
