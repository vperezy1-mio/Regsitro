import uuid

class Producto:
    def __init__(self, nombrePro, tipoPro, costoPro, cantidadPro):
        self.idPro = uuid.uuid4()
        self.nombrePro = nombrePro
        self.tipoPro = tipoPro
        self.costoPro = costoPro
        self.cantidadPro = cantidadPro

    def costoTotal(self):
        return self.costoPro * self.cantidadPro


        """import uuid

class Producto:

    def __nit__(self, nombrePro, tipoPro, cantidad, costo):
        self.idProducto = uuid.uuid4()
        self.nombrePro = nombrePro
        self.tipoPro = tipoPro
        self.cantidad = cantidad
        self.costo = costo"""