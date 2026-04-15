from Empresa import Empresa
from Cliente import Cliente
from Producto import Producto
from Vendedor import Vendedor
from TipoPago import TipoPago
from Factura import Factura

import os

def validarSoloLetras(texto):
    while True:
        valor = input(texto)
        if valor.replace(" ", "").isalpha():
            return valor
        else:
            print("ERROR: Solo se permiten letras. Intente nuevamente.")

def validarSoloNumeros(texto):
    while True:
        valor = input(texto)
        if valor.isdigit():
            return int(valor)
        else:
            print("ERROR!: Solo se permiten numeros. Intente nuevamnte.")

def validarDecimal(texto):
    while True:
        try:
            return float(input(texto))
        except ValueError:
            print("ERROR!: Solo se permiten numeros decimales. intente nuevamente.")

def limpiarPantalla():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


class Main():
    def main(self):
        print("=== INGRESO DE FACTURA ===")
        
        #Ingreso de datos de la empresa
        empresa = Empresa(
            validarSoloLetras("\nIngrese el nombre de la empresa: "),
            validarSoloNumeros("Nit de la empresa: "),
            input("Ingrese la direccion de la empresa: "),
            input("Ingrese el correo de la empresa: ")
        )

        #Ingreso de datos del producto
        producto = Producto(
            validarSoloLetras("\nIngrese el tipo de producto: "),
            validarSoloLetras("Ingresar el nombre del producto: "),
            validarDecimal("Ingrese el costo por unidad: "),
            validarSoloNumeros("Ingrese la cantidad: ")
        )

        #Ingreso de datos del cliente
        cliente = Cliente(
            validarSoloNumeros("\nIngese el NIT del cliente: "),
            validarSoloLetras("Ingrese el nombre del cliente: "),
            input("Ingrese la direccion del cliente: "),
            validarSoloNumeros("Ingrese el telefono del cliente: "),
            input("Ingrese el correo del cliente: ")
        )

        #Ingreso de datos del vendedor
        vendedor = Vendedor(
            validarSoloNumeros("\nIngrese el nit del vendedor: "),
            validarSoloLetras("Ingresar el nombre del vendedor: "),
            validarSoloNumeros("Ingresar la caja de cobro: "),
            validarSoloLetras("Ingresar el turno del vendedor: ")
        )

        #Ingreso del tipo de pago
        print("\nIngrese el tipo de pago:")
        metodo = input("¿Es tarjeta? (si/no): ").lower()
        pago = TipoPago(metodo == "si")

        #Creacion de la factura
        factura = Factura(empresa, cliente, vendedor, producto, pago)

        #limpieza de lapantalla para imprimir los datos
        limpiarPantalla()

        #Impresion de la factura
        factura.imprimirFactura()
        




if __name__ == "__main__":
    app = Main()
    app.main()












"""class Main():
@staticmethod
def main();"""

"""
from Factura import Factura

if __name__ == "__main__":
    print("=== INGRESO DE FACTURA ===")

    # Datos de la factura
    idFactura = int(input("Ingrese el numero de la factura: "))
    fecha = input("Ingrese la fecha de emision: ")

    # Datos de la empresa
    idEmpresa= input("Ingrese el NIT de la empresa: ")
    nombreEm = input("Ingrese el nombre de la empresa: ")
    direccionEm = input("Ingrese direccion de la empresa: ")
    telefonoEm = input("Ingrese telefono de la empresa: ")
    correoEm = input("Ingrese correo de la empresa: ")

    # Datos del vendedor
    idVendedor = int(input("Ingrese el ID del vendedor: "))
    nombreVen = input("Ingrese el nombre del vendedor: ")
    turno = input("Ingrese turno del vendedor: ")
    caja = input("Ingrese caja del vendedor: ")
    telefonoVen = input("Ingrese telefono del vendedor: ")

    # Datos del cliente
    nit = input("Ingrese el NIT del cliente: ")
    nombreCo = input("Ingrese el nombre del cliente: ")
    telefonoCliente = input("Ingrese telefono del cliente: ")
    direccionCliente = input("Ingrese direccion del cliente: ")

    # Datos del producto
    idProducto = int(input("Ingrese el ID del producto: "))
    nombrePro = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio: "))

    total = precio  # por ahora un solo producto

    # Crear la factura
    factura = Factura(
        idFactura, fecha,
        idEmpresa, nombreEm, idVendedor, nombreVen,
        nit, nombreCo,
        idProducto, nombrePro, precio, total
    )

    # Mostrar factura
    print("=== FACTURA GENERADA ===")
    factura.LlenarFactura()
    """