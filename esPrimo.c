/*Crear una función "esPrimo", este recibe un numero, devuelve 1 si es primo o 0 en caso conrario
Chong Santiago Hungman Emmanuel
12/07/2024*/

#include <stdio.h>

// Declaración de la función
int esPrimo(int num);

int main() {
    int num;
    printf("Ingrese un numero: ");
    scanf("%d", &num);
    
    int resultado = esPrimo(num);
    printf("%d\n", resultado);
    
    return 0;
}

// Definición de la función
int esPrimo(int num) {
    if (num <= 1) {
        return 0;
    }
    for (int i = 2; i <= num/2; i++) {
        if (num % i == 0) {
            return 0;
        }
    }
    return 1;
}