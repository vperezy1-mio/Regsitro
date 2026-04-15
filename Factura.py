import uuid
import datetime


class Factura:
    def __init__(self, empresa, cliente, vendedor, producto, tipoPago):
        self.idFactura = uuid.uuid4()
        self.fecha = datetime.datetime.now()
        self.empresa = empresa
        self.cliente = cliente
        self.vendedor = vendedor
        self.producto = producto
        self.tipoPago = tipoPago

    def imprimirFactura(self):
        print(f"\n==== FACTURA ====")
        print(f"Factura ID: {self.idFactura}")
        print(f"Fecha de facturacion: {self.fecha}")

        print(f"\n====DATOS DE LA EMPRESA====")
        print(f"Nombre: {self.empresa.nombreEmp}")
        print(f"Nit: {self.empresa.nitEmp}")
        print(f"Direccion: {self.empresa.direccionEmp}")
        print(f"Correo: {self.empresa.correoEmp}")
        
        print(f"\n====DATOS DEL PRODUCTO====")
        print(f"Tipo: {self.producto.tipoPro}")
        print(f"Nombre: {self.producto.nombrePro}")
        print(f"Costo por unidad: {self.producto.costoPro}")
        print(f"Cantidad: {self.producto.cantidadPro}")

        print(f"\n====DATOS DEL CLIENTE====")
        print(f"Nit: {self.cliente.nitClien}")
        print(f"Nombre: {self.cliente.nombreClien}")
        print(f"Direccion: {self.cliente.direccionClien}")
        print(f"Telefono: {self.cliente.telefonoClien}")
        print(f"Correo: {self.cliente.correoClien}")


        print(f"\n====DATOS DEL VENDEDOR====")
        print(f"Nit: {self.vendedor.nitVen}")
        print(f"Nombre: {self.vendedor.nombreVen}")
        print(f"Caja: {self.vendedor.caja}")
        print(f"Turno: {self.vendedor.turno}")

        print("\n====TIPO DE PAGO====")
        metodo = "Tarjeta" if self.tipoPago.esTarjeta else "Efectivo"
        print(f"Metodo: {metodo}")

        print(f"\n====TOTAL A PAGAR====")
        print(f"Total: {self.producto.costoTotal():.2f}")

    


"""import Empresa
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
"""