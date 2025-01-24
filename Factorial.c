/*Create an program calculate the factorial for all nunmbers
Chong Santiago Hungman Emmanuel
14/06/2024*/

#include <stdio.h>

// Function to calculate the factorial of a number
int factorial(int n) {
    int result = 1;
    for (int i = 1; i <= n; i++) {
        result *= i;
    }
    return result;
}

int main() {
    int num;

    // Input the number
    printf("Introduce un numero: ");
    if (scanf("%d", &num) != 1) {
        printf("Entrada invalida.\n");
        return 1;
    }

    // Check if the number is negative
    if (num < 0) {
        printf("El factorial no está definido para numeros negativos.\n");
    } else {
        // Calculate and print the factorial
        printf("El factorial de %d es %d\n", num, factorial(num));
    }

    return 0;
}