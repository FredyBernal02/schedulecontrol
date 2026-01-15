from flask import Blueprint, request, jsonify
from app import db
from app.models.negocio import Negocio
from datetime import datetime

negocios_bp = Blueprint('negocios', __name__)

@negocios_bp.route('/negocios', methods=['POST'])
def crear_negocio():
    data = request.get_json()

    negocio = Negocio(
        nombre=data['nombre'],
        hora_apertura=datetime.strptime(data['hora_apertura'], '%H:%M').time(),
        hora_cierre=datetime.strptime(data['hora_cierre'], '%H:%M').time()
    )

    db.session.add(negocio)
    db.session.commit()

    return jsonify({'mensaje': 'Negocio creado correctamente'}), 201