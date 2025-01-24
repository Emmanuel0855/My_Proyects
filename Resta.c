/*Función de "resta"
Chong Santiago Hungman Emmanuel
08/07/2024 */

#include <stdio.h>

// Función para restar dos números
int resta(int a, int b) {
    return a - b;
}

int main() {
    int num1, num2;
    
    // Ejemplo de uso de la función resta
    printf("Ingrese dos numeros para restar: ");
    scanf("%d %d", &num1, &num2);
    printf("El resultado de la resta es: %d\n", resta(num1, num2));
    
    return 0;
}
