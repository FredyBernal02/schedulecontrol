from app.extensions import db

class Cliente(db.Model):
    __tablename__ = 'clientes'

    id_cliente = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(120))
    telefono = db.Column(db.String(20))

    id_negocio = db.Column(
        db.Integer,
        db.ForeignKey('negocios.id_negocio'),
        nullable=False
    )