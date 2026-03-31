import uuid

class Empresa:

    def __init__(self, nombreEm, direccion, telefono, correo):
        self.idEmpresa = uuid.uuid4()
        self.nombreEm = nombreEm
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo