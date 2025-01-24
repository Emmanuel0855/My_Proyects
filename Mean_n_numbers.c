/*Calculate the mean of the first n numbers
Chong Santiago Hungman Emmanuel
21/06/2024*/

#include <stdio.h>

int main() {
    int n, i = 1; //Declare Variables
    double suma = 0.0, media;

    printf("Ingresa el valor: "); //Solicitate information  
    scanf("%d", &n);

    do {
        suma += i; // Realiza the sum
        i++;
    } while (i <= n);

    media = suma / n; // Realize the mean operaions

    printf("La media de los primeros %d numeros es: %.2f\n", n, media);

    return 0;
}

