# Generador de Boletas para MYJ ALFAJORES

Este es un script simple en Python para generar una **representación visual de una boleta de venta en formato PDF** para el emprendimiento "MYJ ALFAJORES".

**¡Importante!** Este script solo genera un archivo PDF con el formato de una boleta. Para emitir **boletas electrónicas válidas en Chile**, necesitas un sistema certificado por el Servicio de Impuestos Internos (SII). Este proyecto no se integra con el SII y, por lo tanto, no genera documentos tributarios válidos.

## Características

* **Nombre del Emprendimiento:** MYJ ALFAJORES
* **Datos de la Boleta:** Número de Boleta y Fecha actual.
* **Datos del Cliente:** Nombre, RUT y Dirección.
* **Detalles del Producto:** Nombre, Cantidad, Precio Unitario y Subtotal por cada ítem.
* **Total de la Boleta.**
* **Descarga en PDF** utilizando la librería `ReportLab`.

## Requisitos

Asegúrate de tener **Python** instalado en tu sistema (versión 3.6 o superior es recomendada).

## Instalación

1.  **Clona este repositorio** en tu máquina local o descarga los archivos `main.py` y `requirements.txt`.

    ```bash
    git clone [https://github.com/tu_usuario/nombre_de_tu_repositorio.git](https://github.com/tu_usuario/nombre_de_tu_repositorio.git)
    cd nombre_de_tu_repositorio
    ```

2.  **Instala las dependencias** necesarias utilizando `pip`:

    ```bash
    pip install -r requirements.txt
    ```

## Uso

1.  **Abre el archivo `main.py`** con tu editor de código preferido.
2.  **Modifica los datos del cliente** y la lista de **productos** en la sección `if __name__ == "__main__":` para que reflejen la boleta que deseas generar.

    ```python
    if __name__ == "__main__":
        productos_ejemplo = [
            {"nombre": "Alfajor de Maicena", "cantidad": 6, "precio_unitario": 800},
            {"nombre": "Alfajor de Chocolate", "cantidad": 4, "precio_unitario": 950},
            {"nombre": "Caja de Alfajores Surtidos (x12)", "cantidad": 1, "precio_unitario": 9000},
        ]

        boleta_ejemplo = Boleta(
            numero_boleta="0001",
            fecha=datetime.now(),
            nombre_cliente="Juan Pérez",
            rut_cliente="12.345.678-9",
            direccion_cliente="Calle Falsa 123, Comuna, Ciudad",
            productos=productos_ejemplo
        )
        
        boleta_ejemplo.generar_pdf("boleta_myj_alfajores_0001.pdf")
        print("Boleta generada exitosamente como boleta_myj_alfajores_0001.pdf")
    ```

3.  **Ejecuta el script** desde tu terminal:

    ```bash
    python main.py
    ```

4.  Se generará un archivo PDF con la boleta en el mismo directorio donde ejecutes el script. El nombre del archivo se definirá en el script (por ejemplo, `boleta_myj_alfajores_0001.pdf`).

## Personalización

Si quieres adaptar este generador, puedes modificar el archivo `main.py` para:

* **Cambiar el diseño** o la información adicional en la boleta (fuentes, colores, posiciones, etc.).
* **Añadir más campos**, como métodos de pago, descuentos o información de contacto.
* Considerar la **integración con una base de datos** si necesitas gestionar clientes y productos de forma más estructurada.

## Contribuciones

¡Las contribuciones son bienvenidas! Si tienes ideas para mejorar este generador de boletas, no dudes en abrir un *issue* o enviar un *pull request*.

## Licencia

Este proyecto está bajo la **Licencia MIT**. Consulta el archivo `LICENSE` (si decides incluir uno) para más detalles.
