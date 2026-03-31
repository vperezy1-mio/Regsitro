import uuid

class tipoPago:

    def __init__(self, esTarjeta):
        self.idPago = uuid.uuid4()
        self.esTarjeta = esTarjeta