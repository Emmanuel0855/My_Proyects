/*Que lea 10 numeros por teclado, los almacene en un array y muestre suma, resta y multiplicacion
Chong Santiago Hungman Emmanuel
19/07/2024*/

#include <stdio.h>

int Numeros[10];

int main () {
int suma=0;
int resta=0;
int mult=1;
printf ("Input the numbers");
for (int i=0;i<10;i++) {
    printf ("\nElement %d: ",i);
    scanf("%d",&Numeros[i]);
    suma+= Numeros[i]; 
    resta-= Numeros[i]; 
    mult*= Numeros[i];  
    }
printf ("\nSuma %d, Resta %d, multiplicacion %d.", suma, resta, mult);

return 0;
}