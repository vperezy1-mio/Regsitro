import Empresa
import Vendedor
import Cliente
import TipoPago
import Producto

class Factura:

    def __init__(self, idFactura, fecha, idEmpresa, nombreEm, idVendedor, nombreVen, nit, nombreCo, idProducto, nombrePro, precio, total):
        self.idProducto = idFactura
        super().__init__(idEmpresa)
        super().__init__(nombreEm)
        super().__init__(idVendedor)
        super().__init__(nombreVen)
        super().__init__(nit)
        super().__init__(nombreCo)
        super().__init__(idProducto)
        super().__init__(nombrePro)
        self.fecha = fecha
        super().__init__(precio)
        self.total = total

    def total(self):
        print("Total: {self.total}")

    def LlenarFactura(self):
        print("Factura: {sel.idFactura}")
        print("Nit de la empresa: {self.idEmpresa}")
        print("nombreEm dela empresa: {self.nombreEm}")
        print("Nombre del vendedor: {self.nombreVen}")
        print("Nit cliente: {self.nit}")
        print("NOmbre del cliente: {self.nombreCo}")
        print("Fecha de emision: {self.fecha}")
        print("{self.nombrePro} {self.precio}")
        self.total()
