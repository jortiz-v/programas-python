# Examen Primer Parcial - p45–primer-examen-parcial
total_ventas = 0
continuar = "s"

while continuar.lower() == "s":
    print("Universidad Patito SA de CV")
    print("Sistema de Inscripción Congreso de Sistemas")
    
    # Solicitar tipo de usuario
    print("Tipo de usuario: [1] Alumno $100, [2] Trabajador $200, [3] Docente $500")
    tipo_usuario = int(input("¿Cuál es tu tipo de usuario? "))
    
    if tipo_usuario == 1:
        precio_usuario = 100
        descripcion_usuario = "Alumno"
    elif tipo_usuario == 2:
        precio_usuario = 200
        descripcion_usuario = "Trabajador"
    elif tipo_usuario == 3:
        precio_usuario = 500
        descripcion_usuario = "Docente"
    else:
        print("Opción no válida")
        continue
    
    # Solicitar tipo de paquete
    print("Tipo de paquete: [1] Solo conferencias $600, [2] Con eventos sociales $800, [3] Con kit de acceso $900")
    tipo_paquete = int(input("¿Cuál es tu tipo de paquete? "))
    
    if tipo_paquete == 1:
        precio_paquete = 600
        descripcion_paquete = "Solo conferencias"
    elif tipo_paquete == 2:
        precio_paquete = 800
        descripcion_paquete = "Con eventos sociales"
    elif tipo_paquete == 3:
        precio_paquete = 900
        descripcion_paquete = "Con kit de acceso"
    else:
        print("Opción no válida")
        continue
    
    # Solicitar cantidad
    cantidad = int(input("Cantidad de inscripciones: "))
    
    # Calcular el subtotal
    subtotal = (precio_usuario + precio_paquete) * cantidad
    
    # Calcular el descuento
    descuento = 0
    if subtotal > 5000:
        if tipo_usuario == 1:
            descuento = 0.20 * subtotal
        elif tipo_usuario == 2:
            descuento = 0.10 * subtotal
        elif tipo_usuario == 3:
            descuento = 0.05 * subtotal
    
    total = subtotal - descuento
    
    # Mostrar los resultados de la compra
    print(f"Tu pedido fue: {cantidad}, Tipo de usuario: {descripcion_usuario}, Tipo de paquete: {descripcion_paquete}")
    print(f"Subtotal: {subtotal} con un descuento de: {descuento:.2f} y un total de {total:.2f}")
    
    # Acumular el total de ventas
    total_ventas += total
    
    # Preguntar si desea continuar
    continuar = input("¿Deseas continuar (S/N)? ")

# Mostrar el total de ventas al final del día
print(f"Importe Total de la Venta: {total_ventas:.2f}")
print("Proceso terminado ...")
