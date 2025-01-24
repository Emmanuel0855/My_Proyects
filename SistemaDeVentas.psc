Proceso SistemaDeVentas
    // Paso 1: Ingresar al sistema de ventas
    Escribir "Bienvenido al sistema de ventas."
	
    // Paso 2: Preguntar cuántos productos tiene en el carrito de compras
    Escribir "¿Cuántos productos tienes en tu carrito de compras?"
    Leer cantidadProductos
	
    // Inicializar variables
    sumaArticulos <- 0
    respuesta <- "SI"
    respuestaCantidades <- "SI"
    cantidadModificar <- 0 // Asegurar inicialización de la variable como numérica
	
    // Paso 3: Ciclo para agregar los productos
    Para i <- 1 Hasta cantidadProductos Con Paso 1 Hacer
        Escribir "Ingresa el precio del producto ", i
        Leer precioProducto
        sumaArticulos <- sumaArticulos + precioProducto
    FinPara
	
    // Paso 4: Preguntar si desea agregar más productos o modificar cantidades
    Repetir
        // Preguntar si desea agregar productos adicionales
        Escribir "¿Deseas agregar productos adicionales? (SI/NO)"
        Leer respuesta
		
        Si respuesta = "SI" Entonces
            Escribir "¿Cuántos productos adicionales deseas agregar?"
            Leer productosAdicionales
			
            Para i <- 1 Hasta productosAdicionales Con Paso 1 Hacer
                Escribir "Ingresa el precio del producto adicional ", i
                Leer precioProducto
                sumaArticulos <- sumaArticulos + precioProducto
            FinPara
        FinSi
		
        // Preguntar si desea modificar las cantidades de productos
        Escribir "¿Deseas modificar las cantidades de productos existentes? (SI/NO)"
        Leer respuestaCantidades
		
        Si respuestaCantidades = "SI" Entonces
            Escribir "¿Cuántos productos deseas modificar?"
            Leer cantidadModificar
			
            Si cantidadModificar > 0 Entonces
                Para i <- 1 Hasta cantidadModificar Con Paso 1 Hacer
                    Escribir "Ingresa el precio actualizado del producto ", i
                    Leer nuevoPrecio
                    sumaArticulos <- sumaArticulos + nuevoPrecio // Ajusta el precio nuevo
                FinPara
            SiNo
                Escribir "No ingresaste una cantidad válida para modificar."
            FinSi
        FinSi
    Hasta Que respuesta = "NO" y respuestaCantidades = "NO"
	
    // Paso 5: Suma de los artículos (ya acumulada)
	
    // Paso 6: Aplicar el cálculo adicional
    descuento <- (sumaArticulos * 10) / 100
    total <- sumaArticulos + descuento
	
    // Mostrar el resultado final
    Escribir "El total de la compra con el cálculo adicional es: ", total
FinProceso