/*Escribe un programa que invierta los elementos de un arreglo.
El arreglo es de tamaño 12, cor datos por parte del usuario
Chong Santiago Hungman Emmanuel
22/07/2024*/

#include <stdio.h>

int main() {
    int arr[12];

    // Solicita los elementos del arreglo
    printf("Ingrese 12 elementos para el arreglo:\n");
    for (int i = 0; i < 12; i++) {
        printf("Elemento %d: ", i + 1);
        scanf("%d", &arr[i]);
    }

    // Invierte los elementos del arreglo
    for (int i = 0; i < 6; i++) {
        int temp = arr[i];
        arr[i] = arr[11 - i];
        arr[11 - i] = temp;
    }

    // Muestra los elementos del arreglo invertido
    printf("El arreglo invertido es:\n");
    for (int i = 0; i < 12; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}