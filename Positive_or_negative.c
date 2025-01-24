/*This program evaluates if a number is positive or negative*/
#include <stdio.h>   //Include the standard input/output header file.

int main () {
    int data;  //Declare an integer
    printf("Input a number:");  //Prompt the user to input a number
    scanf("%d", &data);  //Read and store the user's input in 'data'
    
    if (data > 0) {
        printf("Is a positive number");
	}
    else {
        printf("Is a negative number");  
	}    
    return 0;
}