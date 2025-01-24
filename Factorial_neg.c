/*Escribe un programa que calcule el factorial de un número negativo
Chong Santiago Hungman Emmanuel 
15/07/2024*/

#include <stdio.h>

//declaración de la función

int factorial (int);

int main () {
	int data, result;
	printf("\nGive the Data: ");
	scanf("%d", &data);
	result = factorial (data);
	printf("\nEl factorial es: %d", result);

	return 0;
}
int factorial (int Mydata) {
	if (Mydata == 1) {
		return 1;
	}
	else 
	{
		return (Mydata * factorial (Mydata-1)); 
	}
	//return 1;
}