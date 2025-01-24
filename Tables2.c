/*The use ask what multiplication table wants to show
Chong Santiago Hungman Emmanuel 
24/06/2024*/

#include <stdio.h>

int main() {
    int num, i;

    printf("Ingrese el numero: ");
    scanf("%d", &num);

    printf("\nTable del %d:\n", num);
    for (i = 1; i <= 10; ++i) {
        printf("%d x %d = %d\n", num, i, num * i);
    }

    return 0;
}
