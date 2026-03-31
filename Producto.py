import uuid

class Producto:

    def __nit__(self, nombrePro, tipoPro, cantidad, costo):
        self.idProducto = uuid.uuid4()
        self.nombrePro = nombrePro
        self.tipoPro = tipoPro
        self.cantidad = cantidad
        self.costo = costo