/*Ecribir un código para escribir números comprendidos entre 1 y 1,000 en grupos de 20, solicitando al usuario si quiere continuar o no. (Do While)
Chong Santiago Hungman Emmanuel
17/06/2024*/


#include <stdio.h>

int main() {
    int i = 1;
    char response;

    do {
        // Mostrar 20 números
        for (int j = 0; j < 20 && i <= 1000; j++, i++) {
            printf("%d\n", i);
        }
            printf("Desea continuar (s/n): ");
            scanf(" %c", &response); // El espacio antes de %c es para consumir cualquier carácter de nueva línea pendiente
    } while (response == 's' || response == 'S');

    return 0;
}
