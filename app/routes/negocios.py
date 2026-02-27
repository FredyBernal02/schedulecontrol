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
    nombre = request.form['nombre']
    direccion = request.form['direccion']
    telefono = request.form['telefono']
    hora_apertura = request.form['hora_apertura']
    hora_cierre = request.form['hora_cierre']

    hora_apertura_time = datetime.strptime(hora_apertura, '%H:%M').time()
    hora_cierre_time = datetime.strptime(hora_cierre, '%H:%M').time()

    # ✅ VALIDACIÓN: cierre debe ser mayor que apertura
    if hora_cierre_time <= hora_apertura_time:
        error = "La hora de cierre debe ser mayor que la hora de apertura"
        return render_template(
            "negocios/crear.html",
            error=error,
            form_data=request.form
        ), 400

    negocio = Negocio(
        nombre=nombre,
        direccion=direccion or None,
        telefono=telefono or None,
        hora_apertura=hora_apertura_time,
        hora_cierre=hora_cierre_time
    )

    db.session.add(negocio)
    db.session.commit()

    return redirect('/negocios')

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

    hora_apertura_time = datetime.strptime(hora_apertura, '%H:%M').time()
    hora_cierre_time = datetime.strptime(hora_cierre, '%H:%M').time()

    if hora_cierre_time <= hora_apertura_time:
        error = "La hora de cierre debe ser mayor que la hora de apertura"
        return render_template(
            "negocios/crear.html",
            error=error,
            form_data=request.form
        ), 400

    negocio = Negocio(
        nombre=nombre,
        direccion=direccion or None,
        telefono=telefono or None,
        hora_apertura=hora_apertura_time,
        hora_cierre=hora_cierre_time
    )

    db.session.add(negocio)
    db.session.commit()

    return redirect(url_for('negocios.listar_negocios'))