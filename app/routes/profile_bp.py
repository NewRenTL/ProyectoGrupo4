from flask import Blueprint

from ..controllers.ProfileController1 import profile

profile_bp = Blueprint('profile_bp',__name__)

profile_bp.route('/',methods = ['GET', 'POST'])(profile)