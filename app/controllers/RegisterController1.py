import requests
from flask import request,render_template,redirect
from app import db
from app.models import PagUser

def register():
    if request.method == 'POST':
        nombres = request.form['nombres']
        apellidos = request.form['apellidos']
        correo = request.form['correo']
        contraseña = request.form['contraseña']
        print("TERMINO")
        if nombres == None or apellidos == None or correo == None or contraseña == None:
            return "Falta uno de los datos solicitados Completelos porfavor"
        nuevaUser = PagUser(nombre= nombres,apellido=apellidos,correo=correo,contraseña=contraseña)
        comprobar1 = PagUser.query.filter(PagUser.apellido == apellidos).first()
        comprobar2 = PagUser.query.filter(PagUser.correo == correo).first()

        if comprobar1 != None and comprobar2 != None:
            return "El usuario al parecer ya existe"
        try:
            #Flush
            db.session.add(nuevaUser)
            #Commit
            db.session.commit()
            print("LLEGO")
            return redirect('/profile/?nombres='+str(nombres)+'&apellidos='+str(apellidos)+'&correo='+str(correo))
        except Exception as error:
            print(error)
            return "Al parecer hubo un error al ingresar el nuevo usuario {}".format(error)
    return render_template("Register.html")
