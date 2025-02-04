from infrastructure.db.models.client_model import Client


class ClientRepository:

    # CREATE ['POST']
    @staticmethod
    def create_client(customer_type, status, tax_id, identifier, foreign_reference=None):
        """Crear un nuevo cliente en la base de datos"""

        client = Client.create(
            customer_type=customer_type,
            status=status,
            tax_id=tax_id,
            identifier=identifier,
            foreign_reference=foreign_reference
        )
        return client

    # READ ['GET']
    @staticmethod
    def get_client_by_id(client_id):
        try:
            # Devuelve el cliente que coincida con el id proporcionado.
            return Client.get(Client.id == client_id)
        except Client.Doesnoexist:
            return None

    @staticmethod
    def get_all_clients():
        # Devuelve una lista con todos los clientes.
        return list(Client.select())

    # UPDATE ['PUT']
    @staticmethod
    def update_client(client_id, **Kwargs):

        # Actualizacion de datos del cliente
        query = Client.update(**Kwargs).where(Client.id == client_id)
        # Verificamos las folas afectadas
        update_rows = query.execute()
        return update_rows > 0

    # DELETE ['DELETE']
    @staticmethod
    def delete_client(client_id):
        try:
            client = Client.get(Client.id == client_id)
            client.delete_instance()
            return True
        except Client.Doesnoexist:
            return False
