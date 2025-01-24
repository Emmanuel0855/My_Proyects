/*Create a code to sum all the squares for the first 100 numbers
Chong Santiago Hungman Emmanuel
17/06/2024*/

#include <stdio.h>

int main() {
    int sumadecuadrados = 0;

    // Utilizamos un ciclo for para iterar desde 1 hasta 100 (inclusive)
    for (int i = 1; i <= 100; i++) {
        // Calculamos el cuadrado del número actual y lo sumamos a la variable suma_cuadrados
        sumadecuadrados += i * i;
    }

    // Imprimimos el resultado
    printf("La suma de los cuadrados de los primeros 100 numeros es: %d\n", sumadecuadrados);

    return 0;
}