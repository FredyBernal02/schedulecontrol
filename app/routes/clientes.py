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

@clientes_bp.route('/clientes/<int:id_cliente>', methods=['PUT'])
def actualizar_cliente(id_cliente):
    data = request.get_json()

    cliente = Cliente.query.get(id_cliente)

    if not cliente:
        return jsonify({'mensaje': 'Cliente no encontrado'}), 404

    cliente.nombre = data.get('nombre', cliente.nombre)
    cliente.correo = data.get('correo', cliente.correo)
    cliente.telefono = data.get('telefono', cliente.telefono)

    db.session.commit()

    return jsonify({'mensaje': 'Cliente actualizado correctamente'}), 200

@clientes_bp.route('/clientes/<int:id_cliente>', methods=['DELETE'])
def eliminar_cliente(id_cliente):
    cliente = Cliente.query.get(id_cliente)

    if not cliente:
        return jsonify({'mensaje': 'CLiente no encontrado'}), 404
    
    db.session.delete(cliente)
    db.session.commit()

    return jsonify({'mensaje': 'Cliente eliminado correctamente'}), 200

@clientes_bp.route('/clientes', methods=['GET'])
def listar_clientes():
    clientes = Cliente.query.all()

    resultado = []
    for cliente in clientes:
        resultado.append({
            'id_cliente': cliente.id_cliente,
            'nombre': cliente.nombre,
            'correo': cliente.correo,
            'telefono': cliente.telefono,
            'id_negocio': cliente.id_negocio 
        })

    return jsonify(resultado), 200

    