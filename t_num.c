/*Crear una función que reciba una letra y un número, y escriba un "triángulo" formado por esa letra
Chong Santiago Hungman Emmanuel
12/07/2024*/

#include <stdio.h>

//Declarar la función
void dibujarTriangulo(char letra, int anchura) {
    for (int i = anchura; i > 0; i--) {
        for (int j = 0; j < i; j++) {
            printf("%c", letra);
        }
        printf("\n");
    }
}
//Definición e implementación de la función
int main() {
    char caracter;
    int ancho;

    printf("Ingrese un caracter: ");
    scanf(" %c", &caracter);

    printf("Ingrese la anchura inicial del triangulo: ");
    scanf("%d", &ancho);

    dibujarTriangulo(caracter, ancho);

    return 0;
}
