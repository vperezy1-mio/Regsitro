import uuid

class Vendedor:

    def __init__(self, nombreVen, apellido, turno, caja, telefono):
        self.idVendedor = uuid.uuid4()
        self.nombreVen = nombreVen
        self.apellido = apellido
        self.turno = turno
        self.caja = caja
        self.telefono = telefono