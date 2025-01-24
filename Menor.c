/*Función de "Menor"
Chong Santiago Hungman Emmanuel
08/07/2024 */

#include <stdio.h>

// Función para obtener el menor de dos números enteros
int menor(int a, int b) {
    if (a < b) {
        return a;
    } else {
        return b;
    }
}

int main() {
    int num1, num2;
    
    // Ejemplo de uso de la función menor
    printf("Ingrese dos numeros para obtener el menor: ");
    scanf("%d %d", &num1, &num2);
    printf("El menor de los dos numeros es: %d\n", menor(num1, num2));
    
    return 0;
}
