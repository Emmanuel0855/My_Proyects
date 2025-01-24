/*EXERCISE TWO
Author: DIEGO DE GANTE
Date: 27-05-2024
What do it do: EvenOrOdd
*/

#include <stdio.h>

int main() {
    // Declare a variable to hold the input number
    int num;

    // Prompt the user to input a number
    printf("Enter a number: ");
    scanf("%d", &num);

    // Check if the number is even or odd

    //If the remainder is 0 it is even
    if (num % 2 == 0) {
        printf("The number %d is even \n", num);
    }

    //If the remainder is different to 0 it is even
    else {
        printf("The number %d is odd \n", num);
    }

    return 0;

}