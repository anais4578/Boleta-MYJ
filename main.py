from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import inch
from datetime import datetime

class Boleta:
    def __init__(self, numero_boleta, fecha, nombre_cliente, rut_cliente, direccion_cliente, productos):
        self.nombre_emprendimiento = "MYJ ALFAJORES"
        self.numero_boleta = numero_boleta
        self.fecha = fecha
        self.nombre_cliente = nombre_cliente
        self.rut_cliente = rut_cliente
        self.direccion_cliente = direccion_cliente
        self.productos = productos
        self.total = self._calcular_total()

    def _calcular_total(self):
        return sum(producto['cantidad'] * producto['precio_unitario'] for producto in self.productos)

    def generar_pdf(self, nombre_archivo):
        c = canvas.Canvas(nombre_archivo, pagesize=letter)
        width, height = letter

        # --- Encabezado ---
        c.setFont("Helvetica-Bold", 24)
        c.drawCentredString(width / 2.0, height - 50, self.nombre_emprendimiento)
        c.setFont("Helvetica", 12)
        c.drawCentredString(width / 2.0, height - 70, "¡Deliciosos alfajores para endulzar tu día!")

        # --- Datos de la Boleta ---
        c.setFont("Helvetica", 10)
        c.drawString(50, height - 120, f"Boleta N°: {self.numero_boleta}")
        c.drawString(50, height - 140, f"Fecha: {self.fecha.strftime('%d/%m/%Y %H:%M')}")

        # --- Datos del Cliente ---
        c.drawString(50, height - 180, "Datos del Cliente:")
        c.drawString(70, height - 200, f"Nombre: {self.nombre_cliente}")
        c.drawString(70, height - 220, f"RUT: {self.rut_cliente}")
        c.drawString(70, height - 240, f"Dirección: {self.direccion_cliente}")

        # --- Detalles del Producto ---
        y_position = height - 280
        c.setFont("Helvetica-Bold", 10)
        c.drawString(50, y_position, "Descripción")
        c.drawString(250, y_position, "Cantidad")
        c.drawString(350, y_position, "Precio Unitario")
        c.drawString(480, y_position, "Subtotal")
        y_position -= 15
        c.line(45, y_position, width - 45, y_position)
        y_position -= 10

        c.setFont("Helvetica", 10)
        for producto in self.productos:
            subtotal = producto['cantidad'] * producto['precio_unitario']
            c.drawString(50, y_position, producto['nombre'])
            c.drawString(250, y_position, str(producto['cantidad']))
            c.drawString(350, y_position, f"${producto['precio_unitario']:,.2f}")
            c.drawString(480, y_position, f"${subtotal:,.2f}")
            y_position -= 15

        # --- Total ---
        y_position -= 20
        c.setFont("Helvetica-Bold", 12)
        c.drawRightString(width - 50, y_position, f"TOTAL: ${self.total:,.2f}")

        # --- Pie de página (Opcional) ---
        c.setFont("Helvetica-Oblique", 8)
        c.drawCentredString(width / 2.0, 30, "¡Gracias por tu compra!")

        c.save()

if __name__ == "__main__":
    # Ejemplo de uso
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
        productos=productos_ejemplo # Pasar los productos directamente al inicializar
    )
    
    boleta_ejemplo.generar_pdf("boleta_myj_alfajores_0001.pdf")
    print("Boleta generada exitosamente como boleta_myj_alfajores_0001.pdf")
