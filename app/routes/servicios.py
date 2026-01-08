from flask import Blueprint, request, jsonify
from app import db
from app.models.servicio import Servicio

servicios_bp = Blueprint('servicios', __name__)

@servicios_bp.route('/servicios', methods=['POST'])
def crear_servicio():
    data = request.get_json()

    servicio = Servicio(
        nombre=data['nombre'],
        duracion=data['duracion'],
        precio=data['precio'],
        id_negocio=data['id_negocio']
    )

    db.session.add(servicio)
    db.session.commit()

    return jsonify({'mensaje': 'Servicio creado correctamente'}), 201

@servicios_bp.route('/servicios', methods=['GET'])
def listar_servicios():
    servicios = Servicio.query.all()

    resultado = []
    for servicio in servicios:
        resultado.append({
            'id_servicio': servicio.id_servicio,
            'nombre': servicio.nombre,
            'duracion': servicio.duracion,
            'precio': servicio.precio,
            'id_negocio': servicio.id_negocio
        })
    
    return jsonify(resultado), 200