/*Calculate the average of 3 notes for n students
Chong Santiago Hungman Emmanuel 
23/06/2024*/

#include <stdio.h>

int main() {
    int n, i, j;
    float note1, note2, note3, average;

    printf("Ingrese el numero de estudiantes: ");
    scanf("%d", &n);

    for(i = 0; i < n; i++) {
        printf("Ingrese las 3 notas %d: ", i + 1);
        scanf("%f %f %f", &note1, &note2, &note3);

        average = (note1 + note2 + note3) / 3;
        printf("El promedio de notas %d es: %.2f\n", i + 1, average);
    }

    return 0;
}
