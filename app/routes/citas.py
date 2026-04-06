from flask import render_template, Blueprint, request, jsonify, redirect, url_for
from app import db
from app.models.cita import Cita
from datetime import datetime, timedelta
from sqlalchemy import and_
from app.models.negocio import Negocio
from app.models.cliente import Cliente
from app.models.servicio import Servicio


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

@citas_bp.route('/citas/listar', methods=['GET'])
def listar_citas_front():
    citas = Cita.query.all()
    return render_template('citas/listar.html', citas=citas)

@citas_bp.route('/citas/nuevo', methods=['GET'])
def nueva_cita():
    clientes = Cliente.query.all()
    servicios = Servicio.query.all()
    negocios = Negocio.query.all()

    return render_template(
        'citas/crear.html',
        clientes=clientes,
        servicios=servicios,
        negocios=negocios
    )


@citas_bp.route('/citas/nuevo', methods=['POST'])
def crear_cita_front():
    id_cliente = request.form.get('id_cliente')
    id_servicio = request.form.get('id_servicio')
    id_negocio = request.form.get('id_negocio')
    fecha = request.form.get('fecha')
    hora_inicio = request.form.get('hora')

    servicio = Servicio.query.get(id_servicio)

    hora_inicio_dt = datetime.strptime(hora_inicio, '%H:%M')
    hora_fin_dt = hora_inicio_dt + timedelta(minutes=servicio.duracion)

    cita = Cita(
        id_cliente=id_cliente,
        id_servicio=id_servicio,
        id_negocio=id_negocio,
        fecha=datetime.strptime(fecha, '%Y-%m-%d').date(),
        hora_inicio=hora_inicio_dt.time(),
        hora_fin=hora_fin_dt.time(),
        estado='pendiente'
    )

    db.session.add(cita)
    db.session.commit()

    return redirect(url_for('citas.listar_citas_front'))

@citas_bp.route('/citas/<int:id_cita>/eliminar', methods=['POST'])
def eliminar_cita_front(id_cita):
    cita = Cita.query.get_or_404(id_cita)
    db.session.delete(cita)
    db.session.commit()
    return redirect(url_for('citas.listar_citas_front'))

@citas_bp.route('/citas/<int:id_cita>/editar', methods=['GET'])
def editar_cita(id_cita):
    cita = Cita.query.get_or_404(id_cita)
    clientes = Cliente.query.all()
    servicios = Servicio.query.all()
    negocios = Negocio.query.all()

    return render_template(
        'citas/editar.html',
        cita=cita,
        clientes=clientes,
        servicios=servicios,
        negocios=negocios
    )

@citas_bp.route('/citas/<int:id_cita>/editar', methods=['POST'])
def actualizar_cita_front(id_cita):
    cita = Cita.query.get_or_404(id_cita)

    id_cliente = request.form.get('id_cliente')
    id_servicio = request.form.get('id_servicio')
    id_negocio = request.form.get('id_negocio')
    fecha = request.form.get('fecha')
    hora_inicio = request.form.get('hora')

    servicio = Servicio.query.get(id_servicio)

    if len(hora_inicio) == 5:
        hora_inicio_dt = datetime.strptime(hora_inicio, '%H:%M')
    else:
        hora_inicio_dt = datetime.strptime(hora_inicio, '%H:%M:%S')
    
    hora_fin_dt = hora_inicio_dt + timedelta(minutes=servicio.duracion)

    cita.id_cliente = id_cliente
    cita.id_servicio = id_servicio
    cita.id_negocio = id_negocio
    cita.fecha = datetime.strptime(fecha, '%Y-%m-%d').date()
    cita.hora_inicio = hora_inicio_dt.time()
    cita.hora_fin = hora_fin_dt.time()

    db.session.commit()

    return redirect(url_for('citas.listar_citas_front'))