import re


from flask import render_template,redirect,request

from app.models import PagUser

def profile():
    args = request.args
    nombres = args.get('nombres')
    apellidos = args.get('apellidos')
    correo = args.get('correo')
    nombre1 = {'nombres': nombres}
    apellidos1 = {'apellidos': apellidos}
    correo1 = {'correo': correo}
    if nombres == None or apellidos == None or correo == None:
        return "Falta uno de los datos"
    return render_template('profile.html',nombres=nombre1,apellidos=apellidos1)
