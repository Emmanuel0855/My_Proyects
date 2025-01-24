/*Declare una variable de tipo entero y otra de tipo real, una con el nombre de "x" y otra con el identificador "ÿ"
Chong Santiago Hungman Emmanuel 2309059
31/05/2024*/

#include <stdio.h>

int main() {
    int x;
    float y;

    // Solicitar al usuario que ingrese el valor de la variable entera 'x'
    printf("Ingrese un valor entero para 'x': ");
    scanf("%d", &x);

    // Solicitar al usuario que ingrese el valor de la variable real 'y'
    printf("Ingrese un valor real para 'y': ");
    scanf("%f", &y);

    // Imprimir los valores de las variables
    printf("El valor de x es: %d\n", x);
    printf("El valor de y es: %.2f\n", y);

    return 0;
}
