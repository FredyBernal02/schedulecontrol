from app import db

class Negocio(db.Model):
    __tablename__= 'negocios'

    id_negocio = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    direccion = db.Column(db.String(200))
    telefono = db.Column(db.String(20))