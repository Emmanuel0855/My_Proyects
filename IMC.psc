Algoritmo Índice_de_masa_corporal
	Definir IMC Como Real
	// Solicitar los datos al usuario
        IMPRIMIR "Ingrese su peso en kilogramos:"
        LEER peso
		
        IMPRIMIR "Ingrese su estatura en metros:"
        LEER estatura
		
        IMPRIMIR "Ingrese su edad en años:"
        LEER edad
		
        // Calcular el IMC
        IMC = peso / (estatura * estatura)
		
        // Determinar la condición de riesgo de acuerdo con el IMC
		SI IMC < 18.5 ENTONCES Imprimir riesgo = "Bajo peso"
		FinSi
		Si IMC >= 18.5 Y IMC < 24.9 ENTONCES 
				Imprimir riesgo = "Peso normal"
			FinSi
			
			SI IMC >= 25 Y IMC < 29.9 ENTONCES
					riesgo = "Sobrepeso"
				SINO
					riesgo = "Obesidad"
				FINSI
				
				// Imprimir los resultados
				IMPRIMIR "Su IMC es:" IMC
				IMPRIMIR "Condición de riesgo de enfermedades coronarias:" + riesgo
				
				// Preguntar si el usuario desea repetir el cálculo
				IMPRIMIR "¿Desea realizar otro cálculo? (s/n)"
				LEER respuesta
				
				MIENTRAS respuesta == "s"
					
				FinMientras
	
FinAlgoritmo
