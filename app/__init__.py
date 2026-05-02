from flask import Flask
from app.extensions import db
from app.routes.auth import auth_bp
from app.routes.main import main_bp

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

    return app
