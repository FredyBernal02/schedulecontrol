from flask import Blueprint, render_template, request, redirect, url_for, session
from app.models.usuarios import Usuario

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = request.form.get('correo')
        contrasena = request.form.get('contrasena')

        usuario = Usuario.query.filter_by(correo=correo).first()

        if usuario and usuario.contrasena == contrasena:
            session['usuario_id'] = usuario.id_usuario
            session['usuario_nombre'] = usuario.nombre
            return redirect(url_for('main.dashboard'))
        else:
            return render_template('auth/login.html', error='Credenciales incorrectas')

    return render_template('auth/login.html')

@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))