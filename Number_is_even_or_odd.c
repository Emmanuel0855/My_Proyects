/*Hungman Emmanuel Chong Santiago 
27/05/2024
Write a C program to check whether a number is even or odd
*/

#include <stdio.h>

int main() {
    // Declare a variable to hold the input number
    int num;

    // Prompt the user to input a number
    printf("Enter a number: ");
    scanf("%d", &num);

    // Check if the number is even or odd
    if (num % 2 == 0) {
        printf("The number %d is even.\n", num);
    } else {
        printf("The number %d is odd.\n", num);
    }

    return 0;
}