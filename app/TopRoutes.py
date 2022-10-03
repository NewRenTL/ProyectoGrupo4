import re
from app import db
from app import app
from flask import request,render_template
from app.models import PagUser

@app.route('/')
def index0():
    args = request.args
    nombre = args.get('nombre')
    if(nombre != None and len(nombre) > 0 and nombre != ""):
        print(nombre)
        #sendname = {'nombre1':str(nombre)}
        name = {'nombre':str(nombre)}
        #return "El nombre es {}".format(nombre)
    else:
        #sendname = {'nombre1':'Desconocido'}
        name = {'nombre':"Desconocido"}
    return render_template('diana.html', new=name)


'''
@app.route('/index')
def index1():
    return render_template("diana.html")
'''

'''
@app.route('/index2',methods=['POST','GET'])
def index2():
    return render_template("Register.html")
'''