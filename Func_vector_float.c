/*Escribe una función que reciba un vector de números flotantes y su tamaño, y retorne el promedio de sus elementos
Chong Santiago Hungman Emmanuel 
26/07/2024*/

#include <stdio.h>

float CalcularPromedio(float vector[], int tamano) ;
  
  int main() {
	  int n, i;
	  
	  printf("Ingrese tamano del arreglo: ");
	  scanf("%d", &n);
	  
	  float arr[n];
	  
	  printf("Ingrese %d elementos:\n", n);
	  for (i = 0; i < n; i++) {
		printf("\n Dame el elemento %d: ", i);
		scanf("%f", &arr[i]);
	  }
		
	float promedio = CalcularPromedio(arr, n);
	printf("El promedio de los elementos es: %.2f/n", promedio);
	
  return 0;
}

float CalcularPromedio(float arr[], int n) {
	float sum = 0;
	for (int i = 0; i < n; i++) {
		sum += arr[i];
	}
	return (float) sum / n;
}	