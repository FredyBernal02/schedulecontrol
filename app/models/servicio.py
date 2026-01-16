from app.extensions import db

class Servicio(db.Model):
    __tablename__ = 'servicios'

    id_servicio = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    duracion = db.Column(db.Integer, nullable=False) # duración en minutos
    precio = db.Column(db.Float, nullable=False)

    id_negocio = db.Column(
        db.Integer,
        db.ForeignKey('negocios.id_negocio'),
        nullable=False
    )