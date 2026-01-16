from app.extensions import db
from datetime import date, time

class Cita(db.Model):
    __tablename__ = 'citas'

    id_cita = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date, nullable=False)
    hora_inicio = db.Column(db.Time, nullable=False)
    hora_fin = db.Column(db.Time, nullable=False)
    estado = db.Column(db.String(50), nullable=False, default='pendiente')

    id_cliente = db.Column(
        db.Integer,
        db.ForeignKey('clientes.id_cliente'),
        nullable=False
    )

    id_servicio = db.Column(
        db.Integer, 
        db.ForeignKey('servicios.id_servicio'),
        nullable=False
    )

    id_negocio = db.Column(
        db.Integer,
        db.ForeignKey('negocios.id_negocio'),
        nullable=False
    )