/*Hacer todas las funciones en un código
Chong Santiago Hungman Emmanuel
08/07/2024 */

#include <stdio.h>

// Función para restar dos números
int resta(int a, int b) {
    return a - b;
}

// Función para obtener el menor de dos números enteros
int menor(int a, int b) {
    if (a < b) {
        return a;
    } else {
        return b;
    }
}

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

// Función para calcular la potencia de un número entero
int eleva(int base, int exponente) {
    int resultado = 1;
    for (int i = 0; i < exponente; i++) {
        resultado *= base;
    }
    return resultado;
}

int main() {
    int num1, num2, num3;
    
    // Ejemplo de uso de las funciones
    printf("Ingrese dos numeros para restar: ");
    scanf("%d %d", &num1, &num2);
    printf("El resultado de la resta es: %d\n", resta(num1, num2));
    
    printf("Ingrese dos numeros para obtener el menor: ");
    scanf("%d %d", &num1, &num2);
    printf("El menor de los dos numeros es: %d\n", menor(num1, num2));
    
    printf("Ingrese tres numeros para obtener el mayor: ");
    scanf("%d %d %d", &num1, &num2, &num3);
    printf("El mayor de los tres numeros es: %d\n", mayor(num1, num2, num3));
    
    printf("Ingrese la base y el exponente para elevar un numero: ");
    scanf("%d %d", &num1, &num2);
    printf("El resultado de elevar %d a la %d es: %d\n", num1, num2, eleva(num1, num2));
    
    return 0;
}
