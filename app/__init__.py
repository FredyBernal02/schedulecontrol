from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///schedulecontrol.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from app.routes.clientes import clientes_bp
    app.register_blueprint(clientes_bp)

    from app.routes.servicios import servicios_bp
    app.register_blueprint(servicios_bp)

    return app
