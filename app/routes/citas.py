from flask import Blueprint, request, jsonify
from app import db
from app.models.cita import Cita
from datetime import datetime

citas_bp = Blueprint('citas', __name__)

@citas_bp.route('/citas', methods=['POST'])
def crear_cita():
    data = request.get_json()

    cita = Cita(
        fecha=datetime.strptime(data['fecha'], '%Y-%m-%d').date(),
        hora_inicio=datetime.strptime(data['hora_inicio'], '%H:%M').time(),
        hora_fin=datetime.strptime(data['hora_fin'], '%H:%M').time(),
        estado=data.get('estado', 'pendiente'),
        id_cliente=data['id_cliente'],
        id_servicio=data['id_servicio'],
        id_negocio=data['id_negocio']
    )

    db.session.add(cita)
    db.session.commit()

    return jsonify({'mensaje': 'Cita creada correctamente'}), 201

@citas_bp.route('/citas', methods=['GET'])
def listar_citas():
    citas = Cita.query.all()

    resultado = []
    for cita in citas:
        resultado.append({
            'id_cita': cita.id_cita,
            "fecha": cita.fecha.isoformat(),
            'hora_inicio': cita.hora_inicio.strftime('%H:%M'),
            'hora_fin': cita.hora_fin.strftime('%H:%M'),
            'estado': cita.estado,
            'id_cliente': cita.id_cliente,
            'id_servicio': cita.id_servicio,
            'id_negocio': cita.id_negocio
        })
    
    return jsonify(resultado), 200