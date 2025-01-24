/*Create a code to obtain the average for the calification for 15 students
Chong Santiago Hungman Emmanuel
17/06/2024*/

#include <stdio.h>

int main () {
	int suma = 0;
	int Calificaciones;
	int numerodeEstudiantes = 15;
	float Promedio;
	for(int i=0; i < numerodeEstudiantes; i++) {
		printf("Ingrese las Calificaciones: ");
		scanf("%d", &Calificaciones);
		suma += Calificaciones;
	}
	Promedio = (float) suma / numerodeEstudiantes;
	printf("El promedio de las calificaciones del grupo es: %.2f\n", Promedio);

return 0;
}