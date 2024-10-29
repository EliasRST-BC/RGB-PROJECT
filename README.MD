# Tienda de Ropa con POO en Python

## Descripción
Este proyecto implementa un sistema de compra de ropa utilizando Programación Orientada a Objetos (POO) en Python. Permite al usuario seleccionar productos, añadirlos a un carrito de compras y mostrar un resumen de la compra.

## Estructura de Clases

1. **Producto**: Clase base para cualquier producto en la tienda.
   - Atributos: `nombre`, `precio`, `cantidad`.
   - Métodos: `mostrar_info`, `reducir_stock`, y métodos getters para obtener y actualizar atributos.

2. **Ropa**: Clase que hereda de `Producto` y añade características específicas de ropa como `talla` y `tipo_tela`.

3. **Clases derivadas de Ropa**:
   - **Camisa**: Hereda de `Ropa` y añade el atributo `estilo`.
   - **Pantalon**: Hereda de `Ropa` y añade el atributo `largo`.
   - **Zapato**: Hereda directamente de `Producto` y añade el atributo `talla`.

4. **Carrito**: Clase que representa un carrito de compras.
   - Atributos: `productos` (lista de productos seleccionados).
   - Métodos: `agregar_producto`, `mostrar_resumen`.

5. **Tienda**: Clase que maneja la interacción con el usuario y los productos disponibles.
   - Atributos: `productos` (lista de productos en la tienda) y `carrito`.
   - Métodos: `agregar_producto`, `mostrar_productos`, `seleccionar_producto`, `procesar_compra`.

## Principios de POO
- **Encapsulamiento**: Los atributos de `Producto` están encapsulados y se acceden mediante métodos getters y setters.
- **Herencia**: La clase `Ropa` hereda de `Producto`, y `Camisa` y `Pantalon` heredan de `Ropa`.
- **Polimorfismo**: Cada clase hija sobrescribe el método `mostrar_info` para mostrar información específica.
- **Abstracción**: La clase `Tienda` abstrae el proceso de compra.

## Ejemplo de Uso
```python
# Agregar productos a la tienda
tienda.agregar_producto(camisa)
tienda.agregar_producto(pantalon)
tienda.agregar_producto(zapato)

# Mostrar productos y realizar compras
tienda.mostrar_productos()
tienda.seleccionar_producto(1, 2)  # Seleccionar 2 camisas
tienda.procesar_compra()  # Mostrar resumen de compra
