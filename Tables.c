/*A code used for show all the multiplication tables
Chong Santiago Hungman Emmanuel 
24/06/2024*/

#include <stdio.h>

int main() {
    int num, i; //Declaro mis variables

    printf("Tablas de multiplicar:\n"); //Solicito mi operación 

    for (num = 1; num <= 10; ++num) { //Operaciones realizadas y organizadas
        printf("\nTabla del %d:\n", num);  
        for (i = 1; i <= 10; ++i) {
            printf("%d x %d = %d\n", num, i, num * i);
        }
    }

    return 0;
}
