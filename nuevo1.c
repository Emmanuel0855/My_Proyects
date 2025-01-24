#include <stdio.h>

int main() {
    int number;

    // Prompt the user for input
    printf("Please enter an integer number: ");
    
    // Read the integer input from the user
    scanf("%d", &number);

    // Determine if the number is even or odd
    if (number % 2 == 0) {
        // The number is even
        printf("The number %d is even.\n", number);
    } else {
        // The number is odd
        printf("The number %d is odd.\n", number);
    }

    return 0;
}
