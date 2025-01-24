/*EXERCISE ONE
Author: DIEGO DE GANTE
Date: 27-05-2024
What do it do: Maximum number
*/

#include <stdio.h>

int main() {
    int num1, num2, num3;

    //Prompt the user to input the numbers
    printf("Enter three numbers that you want: \n");
    scanf("%d %d %d", &num1, &num2, &num3);

    // Determine the maximum number
    	//If the maximum number is the first
    if (num1 >= num2 && num1 >= num3) {
        printf("The maximum number is: %d\n", num1);

    	//If the maximum number is the second
    } else if (num2 >= num1 && num2 >= num3) {
        printf("The maximum number is: %d\n", num2);

    	//If the maximum number is the third
    } else {
        printf("The maximum number is: %d\n", num3);
    }

    return 0;
}
