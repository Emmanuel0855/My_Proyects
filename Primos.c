/*Hacer un programa en C que lea un número entero positivo de dos dígitos y determinar si sus dígitos son números primos
Chong Santiago Hungman Emmanuel
10/06/2024*/

#include <stdio.h>

int main() {
    int numero;
    int digito1, digito2;

    // Pedir al usuario que ingrese un número de dos dígitos
    printf("Ingrese un numero entero positivo de dos digitos: ");
    scanf("%d", &numero);

    // Verificar si el número está dentro del rango de dos dígitos
    if (numero < 10 || numero > 99) {
        printf("El numero ingresado no es de dos digitos.\n");
        return 1;
    }

    // Separar el número en dos dígitos
    digito1 = numero / 10; // Dígito de las decenas
    digito2 = numero % 10; // Dígito de las unidades

    // Verificar si los dígitos son primos
    if (digito1 == 2 || digito1 == 3 || digito1 == 5 || digito1 == 7) {
        printf("El digito de las decenas (%d) es primo.\n", digito1);
    } else {
        printf("El digito de las decenas (%d) no es primo.\n", digito1);
    }

    if (digito2 == 2 || digito2 == 3 || digito2 == 5 || digito2 == 7) {
        printf("El digito de las unidades (%d) es primo.\n", digito2);
    } else {
        printf("El digito de las unidades (%d) no es primo.\n", digito2);
    }

    return 0;
}
