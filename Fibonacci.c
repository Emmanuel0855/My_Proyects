/*Escribe un programa que calcule el número dado con base al sistema de Fibonacci
Chong Santiago Hungman Emmanuel 
15/07/2024*/

#include <stdio.h>

// Function to calculate the Fibonacci number at a given position
unsigned long long fibonacci(int n) {
    if (n == 0) return 0;
    if (n == 1) return 1;

    unsigned long long a = 0, b = 1, fib = 1;

    for (int i = 2; i <= n; i++) {
        fib = a + b;
        a = b;
        b = fib;
    }

    return fib;
}

int main() {
    int n;
    
    // Ask the client for the position of the Fibonacci number
    printf("Enter the position of the Fibonacci number: ");
    scanf("%d", &n);

    if (n < 0) {
        printf("Position must be a non-negative integer.\n");
        return 1;
    }

    // Calculate and display the Fibonacci number at the given position
    unsigned long long result = fibonacci(n);
    printf("Fibonacci number at position %d is %llu\n", n, result);

    return 0;
}
