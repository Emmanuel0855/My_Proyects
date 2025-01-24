/*Crear una función para calcular el precio de un producto basándose en el precio base del mismo y el impuesto aplicable
Chong Santiago Hungman Emmanuel
12/07/2024*/

#include <stdio.h>

// Función para calcular el precio final del producto
float calcularPrecio(float precioBase, float impuesto) {
    float precioFinal = precioBase * (1 + impuesto);
    return precioFinal;
}

int main() {
    float precioBase, impuesto;

    // Pedir al usuario que ingrese el precio base y el impuesto
    printf("Ingrese el precio base del producto: ");
    scanf("%f", &precioBase);

    printf("Ingrese el impuesto aplicable (porcentaje): ");
    scanf("%f", &impuesto);

    // Convertir el impuesto de porcentaje a decimal (por ejemplo, 15% a 0.15)
    impuesto = impuesto / 100.0;

    // Calcular el precio final llamando a la función calcularPrecio
    float precioFinal = calcularPrecio(precioBase, impuesto);

    // Mostrar el precio final calculado
    printf("El precio final del producto es: %.2f\n", precioFinal);

    return 0;
}