from flask import Blueprint, request, jsonify
from app import db 
from app.models.cliente import Cliente

clientes_bp = Blueprint('clientes', __name__)

@clientes_bp.route('/clientes', methods=['POST'])
def crear_cliente():
    data = request.get_json()

    cliente = Cliente(
        nombre=data['nombre'],
        correo=data.get('correo'),
        telefono=data.get('telefono'),
        id_negocio=data['id_negocio']
    )

    db.session.add(cliente)
    db.session.commit()

    return jsonify({'mensaje': 'Cliente creado correctamente'}), 201