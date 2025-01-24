/*Recibe un carácrter por parte del usuario e indica si es una vocal o un número
Chong Santiago Hungman Emmanuel
10/06/2024
*/

#include <stdio.h>

int main() {
    char Voc;
    printf("Selct: "); 
    scanf("%c", &Voc);

    switch(Voc) {
        case 'A': case 'E': case 'I': case 'O': case 'U':
        case 'a': case 'e': case 'i': case 'o': case 'u':
            printf("Es una vocal\n");
            break;
        case '1': case '2': case '3': case '4': case '5':
        case '6': case '7': case '8': case '9': case '0':
            printf("Es un numero\n");
            break;
        default:
            printf("No es ni una vocal ni un numero\n");
            break;
    }

    return 0;
}