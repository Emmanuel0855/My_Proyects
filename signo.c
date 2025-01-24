/*Crear una función "signo", este recibe un número real, devuelve 1 si es positivo, -1 si es negativo, o 0 en caso de ser cero
Chong Santiago Hungman Emmanuel
12/07/2024*/

#include <stdio.h>

// Declaración de la función
int signo(float numero);

int main() {
    float num;
    printf("Ingrese un numero: ");
    scanf("%f", &num);
    
    int resultado = signo(num);
    printf("El signo de %.2f es: %d\n", num, resultado);
    
    return 0;
}

// Definición de la función
int signo(float numero) {
    if (numero > 0) {
        return 1;
    } else if (numero < 0) {
        return -1;
    } else {
        return 0;
    }
}