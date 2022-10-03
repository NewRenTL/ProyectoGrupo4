from flask import Blueprint

from ..controllers.RegisterController1 import register

register_bp = Blueprint('register_bp',__name__)

register_bp.route('/',methods = ['GET', 'POST'])(register)