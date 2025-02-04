from flask import Flask
from infrastructure.db.db_connection.database import db
from infrastructure.db.models.client_model import Client
from infrastructure.http.controllers.client_controller import client_bp


def create_app():
    app = Flask(__name__)

    # Registro del blueprint del cliente
    app.register_blueprint(client_bp)

    with app.app_context():
        db.connect()
        db.create_tables([Client], safe=True)
        db.close()

        # Conexion a la base de datos antes de cada solicitud
        @app.before_request
        def before_request():
            if db.is_closed():
                db.connect()

    @app.route('/')
    def home():
        return {"message": "Kata Clients API runnig."}


    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)