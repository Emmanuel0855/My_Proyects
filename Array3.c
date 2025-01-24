/*Escribe un programa que cuente el número de elementos pares e impares en un arreglo de números enteros. 
El tamaño del arreglo es de 20 y los elementos deben ser ingresados por el usuario.
Chong Santiago Hungman Emmanuel
22/07/2024*/

#include <stdio.h>

int main() {
    int arr[20];
    int count_even = 0, count_odd = 0;

    // Solicita los elementos del arreglo
    printf("Ingrese 20 elementos para el arreglo:\n");
    for (int i = 0; i < 20; i++) {
        printf("Elemento %d: ", i + 1);
        scanf("%d", &arr[i]);
    }

    // Cuenta el número de elementos pares e impares
    for (int i = 0; i < 20; i++) {
        if (arr[i] % 2 == 0) {
            count_even++;
        } else {
            count_odd++;
        }
    }

    // Muestra el número de elementos pares e impares
    printf("Numero de elementos pares: %d\n", count_even);
    printf("Numero de elementos impares: %d\n", count_odd);

    return 0;
}