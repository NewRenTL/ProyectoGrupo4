from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

app  = Flask(__name__)

app.config.from_object(Config)

db = SQLAlchemy(app)
from app import models,TopRoutes
db.create_all()

from .routes.login_bp import logueo_bp
from .routes.register_bp import register_bp
from .routes.profile_bp import profile_bp

app.register_blueprint(logueo_bp,url_prefix='/login')
app.register_blueprint(register_bp,url_prefix='/register')
app.register_blueprint(profile_bp,url_prefix='/profile')