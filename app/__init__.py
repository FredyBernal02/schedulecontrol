from flask import Flask
from app.extensions import db

def create_app():
    app = Flask(__name__)

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

    return app
