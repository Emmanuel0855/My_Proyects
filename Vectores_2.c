/*Que lea 5 numeros por teclado, los copie a otro array multiplicados por 2 y muestre el segundo array
Chong Santiago Hungman Emmanuel
19/07/2024*/

#include <stdio.h>

int Array1[5];
int Array2[5];

int main () {
 printf("Introduce 5 numeros.");
 for (int i=1; i<=5; i++) {
    printf ("\nNumero %d: ",i);
    scanf("%d",&Array1[i]);
    Array2[i]=Array1[i]*2;
    
 }  
for (int i=1; i<=5;i++) {
        printf ("Number %d=[%d]\n",i,Array2[i]);
}

return 0; 
}