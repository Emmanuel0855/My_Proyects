/*Escribe una función que reciba un vector de enteros y su tamaño, y elimine los elemento duplicados. La función debe retornar el nuevo tamaño del vector.
CHong Santiago Hungman Emmanuel 
26/07/2024*/

#include <stdio.h>

int removerduplicados(int arr[], int n) {
    if (n == 0 || n == 1) {
        return n;
    }

    int temp[n];
    int j = 0;

    for (int i = 0; i < n - 1; i++) {
        if (arr[i] != arr[i + 1]) {
            temp[j++] = arr[i];
        }
    }
    temp[j++] = arr[n - 1];

    for (int i = 0; i < j; i++) {
        arr[i] = temp[i];
    }

    return j;
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

    // Ordenar el vector primero
    for (i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (arr[i] > arr[j]) {
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }

    n = removerduplicados(arr, n);

    printf("Vector despues de eliminar duplicados:\n");
    for (i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\nNuevo tamano del vector: %d\n", n);

    return 0;
}
