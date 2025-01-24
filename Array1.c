/*Escribe un programa que encuentre el valor máximo en un arreglo de números enteros. El tamaño del arreglo y los elementos deben ser ingresados por el usuario.
Chong Santiago Hungman Emmanuel
22/07/2024*/

#include <stdio.h>

int main() {
    int n;

    // Solicita el tamaño del arreglo
    printf("Ingrese el tamano del arreglo: ");
    scanf("%d", &n);

    int arr[n];  // Declarar el arreglo con el tamaño ingresado por el usuario

    // Solicita los elementos del arreglo
    printf("Ingrese los elementos del arreglo:\n");
    for (int i = 0; i < n; i++) {
        printf("Elemento %d: ", i + 1);
        scanf("%d", &arr[i]);
    }

    // Inicializa el valor máximo con el primer elemento del arreglo
    int max = arr[0];

    // Encuentra el valor máximo en el arreglo
    for (int i = 1; i < n; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }

    // Muestra el valor máximo del arreglo
    printf("El valor maximo en el arreglo es: %d\n", max);

    return 0;
}
