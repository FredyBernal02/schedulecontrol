from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from app import db
from app.models.negocio import Negocio
from datetime import datetime

negocios_bp = Blueprint('negocios', __name__)

# RUTA FRONTEND (GET)
@negocios_bp.route('/negocios', methods=['GET'])
def listar_negocios():
    negocios = Negocio.query.all()
    return render_template(
        'negocios/listar.html',
        negocios=negocios
    )

# RUTA API (POST)
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

# RUTA FRONTEND (GET) - formulario
@negocios_bp.route('/negocios/nuevo', methods=['GET'])
def nuevo_negocio():
    return render_template('negocios/crear.html')


# RUTA FRONTEND (POST) - guardar desde formulario
@negocios_bp.route('/negocios/nuevo', methods=['POST'])
def crear_negocio_form():
    nombre = request.form.get('nombre', '').strip()
    direccion = request.form.get('direccion', '').strip()
    telefono = request.form.get('telefono', '').strip()
    hora_apertura = request.form.get('hora_apertura', '').strip()
    hora_cierre = request.form.get('hora_cierre', '').strip()

    negocio = Negocio(
        nombre=nombre,
        direccion=direccion or None,
        telefono=telefono or None,
        hora_apertura=datetime.strptime(hora_apertura, '%H:%M').time(),
        hora_cierre=datetime.strptime(hora_cierre, '%H:%M').time()
    )

    db.session.add(negocio)
    db.session.commit()

    return redirect(url_for('negocios.listar_negocios'))