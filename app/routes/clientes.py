from flask import Blueprint, request, jsonify
from app import db 
from app.models.cliente import Cliente
from flask import render_template
from flask import redirect, url_for
from app.models.negocio import Negocio

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

@clientes_bp.route('/clientes/listar', methods=['GET'])
def listar_clientes_front():
    clientes = Cliente.query.all()
    return render_template('clientes/listar.html', clientes=clientes)

@clientes_bp.route('/clientes/nuevo', methods=['GET'])
def nuevo_cliente():
    negocios = Negocio.query.all()
    return render_template('clientes/crear.html', negocios=negocios)


@clientes_bp.route('/clientes/nuevo', methods=['POST'])
def crear_cliente_front():
    nombre = request.form.get('nombre')
    correo = request.form.get('correo')
    telefono = request.form.get('telefono')
    id_negocio = request.form.get('id_negocio')

    cliente = Cliente(
        nombre=nombre,
        correo=correo,
        telefono=telefono,
        id_negocio=id_negocio
    )

    db.session.add(cliente)
    db.session.commit()

    return redirect(url_for('clientes.listar_clientes_front'))

@clientes_bp.route('/clientes/<int:id_cliente>/editar', methods=['GET'])
def editar_cliente(id_cliente):
    cliente = Cliente.query.get_or_404(id_cliente)
    negocios = Negocio.query.all()
    return render_template('clientes/editar.html', cliente=cliente, negocios=negocios)


@clientes_bp.route('/clientes/<int:id_cliente>/editar', methods=['POST'])
def actualizar_cliente_front(id_cliente):
    cliente = Cliente.query.get_or_404(id_cliente)

    cliente.nombre = request.form.get('nombre')
    cliente.correo = request.form.get('correo')
    cliente.telefono = request.form.get('telefono')
    cliente.id_negocio = request.form.get('id_negocio')

    db.session.commit()

    return redirect(url_for('clientes.listar_clientes_front'))

@clientes_bp.route('/clientes/<int:id_cliente>/eliminar', methods=['POST'])
def eliminar_cliente_front(id_cliente):
    cliente = Cliente.query.get_or_404(id_cliente)
    db.session.delete(cliente)
    db.session.commit()
    return redirect(url_for('clientes.listar_clientes_front'))

    