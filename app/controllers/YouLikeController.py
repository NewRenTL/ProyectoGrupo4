from app import db
from app.models import PagUser
from flask import request

def youLike():
    if request.method == 'POST':
        #Elije una comida respecto a sus ids
        idelegida = request.form['idnueva']
        if idelegida == None or idelegida == "":
            return "Mandar a pagina avisando que no ha colocado bien su eleccion"
        