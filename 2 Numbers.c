/*Ask for two numbers say if they are the same or not*/

#include <stdio.h>

int main() {
    // Declare variables to hold the input numbers
    int num1, num2;

    // Prompt the user to input the first number
    printf("Enter the first number: ");
    scanf("%d", &num1);

    // Prompt the user to input the second number
    printf("Enter the second number: ");
    scanf("%d", &num2);

    // Check if the numbers are the same
    if (num1 == num2) {
        printf("The numbers are the same.\n");
    } else {
        printf("The numbers are not the same.\n");
    }

    return 0;
}
