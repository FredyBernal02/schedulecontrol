from app import create_app, db
from app.models.negocio import Negocio

app = create_app()

with app.app_context():
    db.create_all()
    print("Base de datos creada correctamente")