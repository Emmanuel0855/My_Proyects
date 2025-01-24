/*Función de "Mayor"
Chong Santiago Hungman Emmanuel
08/07/2024 */

#include <stdio.h>

// Función para obtener el mayor de tres números enteros
int mayor(int a, int b, int c) {
    int max = a;
    if (b > max) {
        max = b;
    }
    if (c > max) {
        max = c;
    }
    return max;
}

int main() {
    int num1, num2, num3;
    
    // Ejemplo de uso de la función mayor
    printf("Ingrese tres numeros para obtener el mayor: ");
    scanf("%d %d %d", &num1, &num2, &num3);
    printf("El mayor de los tres numeros es: %d\n", mayor(num1, num2, num3));
    
    return 0;
}

