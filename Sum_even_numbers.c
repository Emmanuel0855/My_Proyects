/*Print the Sum of All the Even Numbers Between 1 - 100 and Say How Many There Are
Chong Santiago Hungman Emmanuel
23/06/2024*/

#include <stdio.h>

int main() {
    int sum = 0;
    int count = 0;

    for(int i = 2; i <= 100; i += 2) {
        sum += i;
        count++;
    }

    printf("La suma de numeros pares del 1 al 100 es: %d\n", sum);
    printf("La cantidad de numeros pares entre 1 y 100 es: %d\n", count);

    return 0;
}
