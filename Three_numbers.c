/*Hungman Emmanuel Chong Santiago 
27/05/2024
Write a C program to find maximum between three numbers, and print in the screen.*/
#include <stdio.h>

int main() {
    // Declare variables to hold the three numbers
    int num1, num2, num3;

    // Prompt the user to input the first number
    printf("Enter the first number: ");
    scanf("%d", &num1);

    // Prompt the user to input the second number
    printf("Enter the second number: ");
    scanf("%d", &num2);

    // Prompt the user to input the third number
    printf("Enter the third number: ");
    scanf("%d", &num3);

    // Determine the maximum number
    int max = num1;

    if (num2 > max) {
        max = num2;
    }
    if (num3 > max) {
        max = num3;
    }

    // Print the maximum number
    printf("The maximum number is: %d\n", max);

    return 0;
}
