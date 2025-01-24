/*Create an program that writes the day of the year
Chong Santiago Hungman Emmanuel
14/06/2024*/

#include <stdio.h>

int main() {
    int day, month, year;
    int daysInMonths[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

    // Ingresar fecha
    printf("Enter day: ");
    scanf("%d", &day);
    printf("Enter month: ");
    scanf("%d", &month);
    printf("Enter year: ");
    scanf("%d", &year);

    // Calcular el día del año
    int dayOfYear = 0;
    for (int i = 0; i < month - 1; i++) {
        dayOfYear += daysInMonths[i];
    }
    dayOfYear += day;

    // Imprimprimir resultado
    printf("The day of the year is: %d\n", dayOfYear);

    return 0;
}