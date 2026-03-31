import uuid

class Cliente:

    def __init__(self, nit, nombreCo, telefono, direccion):
        self.idCliente = uuid.uuid4()
        self.nit = nit
        self.nombreCo = nombreCo
        self.telefono = telefono
        self.direccion = direccion
