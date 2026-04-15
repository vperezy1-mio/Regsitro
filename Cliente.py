import uuid

class Cliente:
    def __init__(self, nitClien, nombreClien, direccionClien, telefonoClien, correoClien):
        self.nitClien = nitClien
        self.nombreClien = nombreClien
        self.direccionClien = direccionClien
        self.telefonoClien = telefonoClien
        self.correoClien = correoClien
        


        """import uuid

class Cliente:

    def __init__(self, nit, nombreCo, telefono, direccion):
        self.idCliente = uuid.uuid4()
        self.nit = nit
        self.nombreCo = nombreCo
        self.telefono = telefono
        self.direccion = direccion

    input("Presiona enter para salir...")#esta linea es para que la terminal de pyhton pueda ejecutar esta clse y no se cierre"""