from flask import Blueprint

from ..controllers.LoginController1 import login

logueo_bp = Blueprint('logueo_bp',__name__)

logueo_bp.route('/',methods = ['GET', 'POST'])(login)