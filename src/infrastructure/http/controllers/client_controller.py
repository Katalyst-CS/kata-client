from flask import Blueprint, request, jsonify

from infrastructure.db.repositories.client_repository import ClientRepository

client_bp = Blueprint('client', __name__)


# Crear cliente
@client_bp.route('/clients', methods=['POST'])
def create_client():
    # Recogida de datos enviados por el usuario
    data = request.get_json()

    # Validar que data sea un diccionario
    if not isinstance(data, dict):
        return jsonify({"error": "El cuerpo de la solicitud debe ser un JSON válido"}),400

    # Validar datos requeridos (posible implementacion de DTO?)
    required_fields = ['customer_type', 'status', 'tax_id', 'identifier']
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Faltan campos obligatorios."}), 400

    # Crear cliente en la base de datos
    client = ClientRepository.create_client(
    customer_type=data['customer_type'],
    status=data['status'],
    tax_id=data['tax_id'],
    identifier=data['identifier']
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


# Lista de todos los clientes
@client_bp.route('/clients', methods=['GET'])
def get_all_clients():
    clients = ClientRepository.get_all_clients()
    client_list = [{
        "id": str(client.id),
        "customer_type": client.customer_type,
        "status": client.status,
        "tax_id": client.tax_id,
        "identifier": client.identifier,
        "foreign_reference": str(client.foreign_reference) if client.foreign_reference else None,
        "date_created": client.date_created.strftime('%Y-%m-%d %H:%M:%S'),
        "date_modified": client.date_modified.strftime('%Y-%m-%d %H:%M:%S'),
    } for client in clients]

    return jsonify(client_list), 200


@client_bp.route('/clients/<client_id>', methods=['GET'])
def get_client_by_id(client_id):
    client = ClientRepository.get_client_by_id(client_id)
    if client is None:
        return jsonify({"error": "Cliente no encontrado"}), 404

    return jsonify({
        "id": str(client.id),
        "customer_type": client.customer_type,
        "status": client.status,
        "tax_id": client.tax_id,
        "identifier": client.identifier,
        "foreign_reference": str(client.foreign_reference) if client.foreign_reference else None,
        "date_created": client.date_created.strftime('%Y-%m-%d %H:%M:%S'),
        "date_modified": client.date_modified.strftime('%Y-%m-%d %H:%M:%S'),
    }), 200