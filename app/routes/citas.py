from flask import Blueprint, request, jsonify
from app import db
from app.models.cita import Cita
from datetime import datetime
from sqlalchemy import and_
from app.models.negocio import Negocio

citas_bp = Blueprint('citas', __name__)

@citas_bp.route('/citas', methods=['POST'])
def crear_cita():
    data = request.get_json()

    negocio = Negocio.query.get(data['id_negocio'])

    if not negocio:
        return jsonify({'mensaje': 'Negocio no encontrado'}), 404
    
    # Validar horario de atencion
    if hora_inicio < negocio.hora_apertura or hora_fin > negocio.hora_cierre:
        return jsonify({
            'mensaje': 'La cita está fuera del horario de atención del negocio'
        }), 400

    # Convertir fecha y horas
    fecha = datetime.strptime(data['fecha'], '%Y-%m-%d').date()
    hora_inicio = datetime.strptime(data['hora_inicio'], '%H:%M').time()
    hora_fin = datetime.strptime(data['hora_fin'], '%H:%M').time()

    # Buscar citas que se crucen en el mismo negocio y fecha
    cita_cruzada = Cita.query.filter(
        Cita.id_negocio == data['id_negocio'],
        Cita.fecha == fecha,
        and_(
            hora_inicio < Cita.hora_fin,
            hora_fin > Cita.hora_inicio
        )
    ).first()

    if cita_cruzada:
        return jsonify({
            'mensaje': 'Ya existe una cita en ese horario para este negocio'
        }), 400

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

@citas_bp.route('/citas/<int:id_cita>', methods=['PUT'])
def actualizar_cita(id_cita):
    data = request.get_json()

    cita = Cita.query.get(id_cita)

    if not cita:
        return jsonify({'mensaje': 'Cita no encontrada'}), 404
    
    if 'fecha' in data:
        cita.fecha = datetime.strptime(data['fecha'], '%Y-%m-%d').date()
    
    if 'hora_inicio' in data:
        cita.hora_inicio = datetime.strptime(data['hora_inicio'], '%H:%M').time()

    if 'hora_fin' in data:
        cita.hora_fin = datetime.strptime(data['hora_fin'], '%H:%M').time()

    if 'estado' in data:
        cita.estado = data['estado']

    db.session.commit()

    return jsonify({'mensaje': 'Cita actualizada correctamente'}), 200

@citas_bp.route('/citas/<int:id_cita>', methods=['DELETE'])
def eliminar_cita(id_cita):
    cita = Cita.query.get(id_cita)

    if not cita:
        return jsonify({'mensaje': 'Cita no encontrada'}), 404
    
    db.session.delete(cita)
    db.session.commit()

    return jsonify({'mensaje': 'Cita eliminada correctamente'}), 200