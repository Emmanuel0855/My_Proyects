/*Escribe un programa que calcule la suma de todos los elementos en un arreglo de enteros. El tamaño del arreglo y los elementos puede ser ingresados por el usuario.
Chong Santiago Hungman Emmanuel
22/07/2024*/

#include <stdio.h>

int main() {
    int n, i, sum = 0;
    
    // Solicita el tamaño del arreglo
    printf("Ingrese el tamano del arreglo: ");
    scanf("%d", &n);

    int arr[n];  // Declarar el arreglo con el tamaño ingresado por el usuario

    // Solicita los elementos del arreglo
    printf("Ingrese los elementos del arreglo:\n");
    for (i = 0; i < n; i++) {
        printf("Elemento %d: ", i + 1);
        scanf("%d", &arr[i]);
    }

    // Calcula la suma de los elementos del arreglo
    for (i = 0; i < n; i++) {
        sum += arr[i];
    }

    // Muestra la suma de los elementos del arreglo
    printf("La suma de los elementos del arreglo es: %d\n", sum);

    return 0;
}