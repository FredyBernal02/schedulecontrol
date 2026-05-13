from flask import Blueprint, render_template, request, redirect, url_for, session
from flask import flash
from app.models.usuarios import Usuario
from werkzeug.security import check_password_hash
from app import db

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = request.form.get('correo')
        contrasena = request.form.get('contrasena')

        usuario = Usuario.query.filter_by(correo=correo).first()

        if usuario and check_password_hash(usuario.contrasena, contrasena):
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

@auth_bp.route('/usuarios/nuevo', methods=['GET'])
def crear_usuario():
    return render_template('auth/crear_usuario.html')

@auth_bp.route('/usuarios/nuevo', methods=['POST'])
def guardar_usuario():
    from app import db
    from app.models.usuarios import Usuario
    from werkzeug.security import generate_password_hash

    nombre = request.form.get('nombre')
    correo = request.form.get('correo')
    contrasena = request.form.get('contrasena')

    usuario_existente = Usuario.query.filter_by(correo=correo).first()

    if usuario_existente:
        flash("Ya existe un usuario registrado con ese correo.", "error")
        return redirect(url_for('auth.crear_usuario'))

    usuario = Usuario(
        nombre=nombre,
        correo=correo,
        contrasena=generate_password_hash(contrasena),
        rol='admin',
        id_negocio=1
    )

    db.session.add(usuario)
    db.session.commit()

    flash("Usuario creado correctamente", "success")

    return redirect(url_for('auth.listar_usuarios'))

@auth_bp.route('/usuarios')
def listar_usuarios():
    if 'usuario_id' not in session:
        return redirect(url_for('auth.login'))

    usuarios = Usuario.query.all()
    return render_template('auth/usuarios.html', usuarios=usuarios)

@auth_bp.route('/usuarios/<int:id_usuario>/eliminar', methods=['POST'])
def eliminar_usuario(id_usuario):
    usuario = Usuario.query.get_or_404(id_usuario)

    if usuario.id_usuario == session.get('usuario_id'):
        flash("No puedes eliminar tu propio usuario", "error")
        return redirect(url_for('auth.listar_usuarios'))

    db.session.delete(usuario)
    db.session.commit()

    flash("Usuario eliminado correctamente", "success")
    return redirect(url_for('auth.listar_usuarios'))

@auth_bp.route('/usuarios/<int:id_usuario>/editar', methods=['GET', 'POST'])
def editar_usuario(id_usuario):
    if 'usuario_id' not in session:
        return redirect(url_for('auth.login'))

    usuario = Usuario.query.get_or_404(id_usuario)

    if request.method == 'POST':
        usuario.nombre = request.form.get('nombre')
        usuario.correo = request.form.get('correo')

        db.session.commit()

        flash('Usuario actualizado correctamente', 'success')
        return redirect(url_for('auth.listar_usuarios'))

    return render_template('auth/editar_usuario.html', usuario=usuario)