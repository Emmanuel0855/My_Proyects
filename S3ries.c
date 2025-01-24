/*Print on screen an incremental series form 0 to 10
Chong Santiago Hungman Emmanuel
21/06/2024*/

#include <stdio.h>

int main() {
    int num_repeticiones;

    // Solicitar al usuario la cantidad de repeticiones
    printf("Ingrese la cantidad de veces que se repita la serie: ");
    scanf("%d", &num_repeticiones);

    // Validar que la cantidad de repeticiones sea mayor a 0
    if (num_repeticiones <= 0) {
        printf("El número de repeticiones debe ser mayor a 0.\n");
        return 1; // Salir del programa con un código de error
    }

    // Imprimir la serie de 10 en 10
    for (int i = 0; i < num_repeticiones; i++) {
        printf("Serie %d: ", i + 1);
        for (int j = 0; j <= 10; j++) {
            printf("%d ", j);
        }
        printf("\n"); // Salto de línea para la siguiente serie
    }

    return 0; // Salir del programa con éxito
}
