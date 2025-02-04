from flask import Blueprint, request, jsonify

from infrastructure.db.repositories.client_repository import ClientRepository

client_bp = Blueprint('client', __name__)


@client_bp.route('/clients', methods=['POST'])
def create_client():
    # Recogida de datos enviados por el usuario
    data = request.get_json()

    # Validar datos requeridos (posible implementacion de DTO?)
    required_fields = ['customer_type', 'status', 'tax_id', 'identifier']
    if not all(field in data for field in required_fields):
        return jsonify({"error:": "Faltan campos obligatorios."}), 400

    # Crear cliente en la base de datos
    client = ClientRepository.create_client(
        customer_type=data('customer_type'),
        status=data('status'),
        tax_id=data('tax_id'),
        identifier=data('identifier')
    )

    # Retornamos respuesta JSON con los datos del cliente introducidos;

    return jsonify({
        "id:": str(client.id),
        "customer_type": str(client.customer_type),
        "status": client.status,
        "tax_id": client.tax_id,
        "identifier": client.identifier,
        "foreign_reference": str(client.foreing_reference) if client.foreign_reference else None,
        "date_created": client.date_created.strftime('%Y-%m-%d %H:%M:%S'),
        "date_modified": client.date_modified.strftime('%Y-%m-%d %H:%M:%S'),
    }), 201 #Codigo 201: created



