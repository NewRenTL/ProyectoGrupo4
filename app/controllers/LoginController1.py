import re


from flask import render_template,redirect,request

from app.models import PagUser

import app

def login():
    if request.method == 'POST':
        correo = request.form["correo"]
        contraseña = request.form["contraseña"]
        if correo == None or contraseña == None:
            return "Diablos falta uno de los datos"
        try:
            usuario = PagUser.query.filter(PagUser.correo == correo).first()
            if usuario == None:
                return "Este usuario o correo no existe"
            return redirect('/profile/?nombres='+str(usuario.nombre)+'&apellidos='+str(usuario.apellido)+'&correo='+str(usuario.correo))
        except Exception as error:
            print(error)
            return "Ha ocurrido un error al logearse {}".format(error)
    return render_template("login.html")