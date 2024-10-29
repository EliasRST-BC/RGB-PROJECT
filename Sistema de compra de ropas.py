# tienda.py

# Clase base Producto con encapsulamiento
class Producto:
    def __init__(self, nombre, precio, cantidad):
        self._nombre = nombre  # Atributo encapsulado
        self._precio = precio
        self._cantidad = cantidad

    def get_nombre(self):
        return self._nombre

    def get_precio(self):
        return self._precio

    def get_cantidad(self):
        return self._cantidad

    def set_cantidad(self, cantidad):
        if cantidad >= 0:
            self._cantidad = cantidad

    def reducir_stock(self, cantidad_vendida):
        if cantidad_vendida <= self._cantidad:
            self._cantidad -= cantidad_vendida

    def mostrar_info(self):
        print(f"Nombre: {self._nombre}, Precio: ${self._precio}, Stock: {self._cantidad}")


# Clase Ropa que hereda de Producto y añade características específicas
class Ropa(Producto):
    def __init__(self, nombre, precio, cantidad, talla, tipo_tela):
        super().__init__(nombre, precio, cantidad)
        self._talla = talla
        self._tipo_tela = tipo_tela

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Talla: {self._talla}, Tipo de tela: {self._tipo_tela}")


# Clases específicas de Ropa (Camisa, Pantalon, Zapato) que heredan de Ropa y añaden atributos particulares
class Camisa(Ropa):
    def __init__(self, nombre, precio, cantidad, talla, tipo_tela, estilo):
        super().__init__(nombre, precio, cantidad, talla, tipo_tela)
        self._estilo = estilo

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Estilo: {self._estilo}")


class Pantalon(Ropa):
    def __init__(self, nombre, precio, cantidad, talla, tipo_tela, largo):
        super().__init__(nombre, precio, cantidad, talla, tipo_tela)
        self._largo = largo

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Largo: {self._largo}")


class Zapato(Producto):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)
        self._talla = talla

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Talla de zapato: {self._talla}")


# Clase Carrito para almacenar productos seleccionados
class Carrito:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto, cantidad):
        if producto.get_cantidad() >= cantidad:
            producto.reducir_stock(cantidad)
            self.productos.append((producto, cantidad))
            print(f"{cantidad} unidad(es) de {producto.get_nombre()} añadida(s) al carrito.")
        else:
            print(f"Stock insuficiente para {producto.get_nombre()}.")

    def mostrar_resumen(self):
        total = 0
        print("\nResumen de Compra:")
        for producto, cantidad in self.productos:
            subtotal = producto.get_precio() * cantidad
            total += subtotal
            print(f"{producto.get_nombre()} x{cantidad} - ${subtotal:.2f}")
        print(f"\nTotal a pagar: ${total:.2f}")


# Clase Tienda para gestionar los productos e interactuar con el usuario
class Tienda:
    def __init__(self):
        self.productos = []
        self.carrito = Carrito()

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        print("\nProductos disponibles:")
        for idx, producto in enumerate(self.productos, start=1):
            print(f"{idx}. ", end="")
            producto.mostrar_info()

    def seleccionar_producto(self, indice, cantidad):
        if 1 <= indice <= len(self.productos):
            producto = self.productos[indice - 1]
            self.carrito.agregar_producto(producto, cantidad)
        else:
            print("Índice de producto no válido.")

    def procesar_compra(self):
        self.carrito.mostrar_resumen()


# Configuración de la tienda y productos
tienda = Tienda()

# Ejemplos de productos
camisa = Camisa("Camisa de Hombre", 25.00, 10, "M", "Algodón", "Casual")
pantalon = Pantalon("Pantalón de Hombre", 30.00, 5, "L", "Jean", "Largo")
zapato = Zapato("Zapatos de Hombre", 60.00, 8, "42")

# Agregar productos a la tienda
tienda.agregar_producto(camisa)
tienda.agregar_producto(pantalon)
tienda.agregar_producto(zapato)

# Interacción con el usuario
tienda.mostrar_productos()
tienda.seleccionar_producto(1, 2)  # Seleccionar 2 camisas
tienda.seleccionar_producto(2, 1)  # Seleccionar 1 pantalón
tienda.procesar_compra()