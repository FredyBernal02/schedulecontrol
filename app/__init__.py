from flask import Flask, session, redirect, url_for, request
from app.extensions import db
from app.routes.auth import auth_bp
from app.routes.main import main_bp
from app.models.usuarios import Usuario
from werkzeug.security import generate_password_hash

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'schedulecontrol_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///schedulecontrol.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from app.routes.clientes import clientes_bp
    from app.routes.servicios import servicios_bp
    from app.routes.citas import citas_bp
    from app.routes.negocios import negocios_bp

    app.register_blueprint(clientes_bp)
    app.register_blueprint(servicios_bp)
    app.register_blueprint(citas_bp)
    app.register_blueprint(negocios_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)

    @app.before_request
    def proteger_rutas():
        rutas_publicas = ['auth.login', 'citas.vista_agendar', 'citas.agendar_publico', 'citas.confirmacion_reserva', 'static']

        if request.endpoint in rutas_publicas:
            return

        if 'usuario_id' not in session:
            return redirect(url_for('auth.login'))

    with app.app_context():
        db.create_all()

        admin = Usuario.query.filter_by(correo="admin@test.com").first()

        if not admin:
            admin = Usuario(
                nombre="Admin",
                correo="admin@test.com",
                contrasena=generate_password_hash("1234"),
                rol="admin",
                id_negocio=1
            )

            db.session.add(admin)
            db.session.commit()

    return app
