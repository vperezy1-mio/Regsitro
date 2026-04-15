import uuid

class Empresa:
    def __init__(self, nitEmp, nombreEmp, direccionEmp, correoEmp):
        self.nitEmp = nitEmp
        self.nombreEmp = nombreEmp
        self.direccionEmp = direccionEmp
        self.correoEmp = correoEmp


        """import uuid

class Empresa:

    def __init__(self, nombreEm, direccion, telefono, correo):
        self.idEmpresa = uuid.uuid4()
        self.nombreEm = nombreEm
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo"""