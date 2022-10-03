from app import db


class PagUser(db.Model):
    __tablename__ = 'UsuariosPagina'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    nombre = db.Column(db.String(100),nullable =False,unique=True)
    apellido = db.Column(db.String(100),nullable =False,unique=True)
    correo = db.Column(db.String(100),nullable =False,unique=True)
    contraseña = db.Column(db.String(30),nullable =False)
    def __repr__(self):
        return '< Usuario {} >'.format(self.nombre)

class EstadisticaPlatos(db.Model):
    nombreComida = db.Column(db.String(50),primary_key=True)
    cantidad = db.Column(db.Integer)
    



