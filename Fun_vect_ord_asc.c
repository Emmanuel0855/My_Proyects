/*Escribe una función que reciba un vector de enteros y su tamaño, y ordene los elemtos en orden ascendente
Chong Santiago Hungman Emmanuel
26/07/2024*/

#include <stdio.h>

void OrdenarVector(int arr[], int n) {
    int i, j, temp;
    for (i = 0; i < n; i++) {
        for (j = i + 1; j < n; j++) {
            if (arr[i] > arr[j]) {
                temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }
}

int main() {
    int n, i;

    printf("Ingrese el tamano del vector: ");
    scanf("%d", &n);

    int arr[n];
    printf("Ingrese los elementos del vector:\n");
    for (i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    OrdenarVector(arr, n);

    printf("Vector ordenado:\n");
    for (i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}
