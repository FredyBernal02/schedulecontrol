from app.extensions import db

class Usuario(db.Model):
    __tablename__='usuarios'

    id_usuario = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(120), unique=True, nullable=False)
    contrasena = db.Column(db.String(200), nullable=False)
    rol = db.Column(db.String(50), nullable=False)

    id_negocio = db.Column(
        db.Integer,
        db.ForeignKey('negocios.id_negocio'),
        nullable=False
    )