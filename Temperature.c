/*Hungman Emmanuel Chong Santiago 
27/05/2024
In the screen print a comment about the temperature of the day*/

#include <stdio.h>   //Include the standard input/output header file.

int main () {
    int temperature;  //Declare an integer
    printf("Input a number:");  //Prompt the user to input a number
    scanf("%d", &temperature);  //Read and store the user's input in 'temperature'
    
    if (temperature < 12) {
        printf("Cold");
	}
	else if (temperature < 28) {
        printf("Medium");  
	}    
	else {
	printf("Heat");
	}
    return 0;
}