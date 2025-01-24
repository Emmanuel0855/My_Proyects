/*Función de "Eleva"
Chong Santiago Hungman Emmanuel
08/07/2024 */

#include <stdio.h>

// Función para calcular la potencia de un número entero
int eleva(int base, int exponente) {
    int resultado = 1;
    for (int i = 0; i < exponente; i++) {
        resultado *= base;
    }
    return resultado;
}

int main() {
    int base, exponente;
    
    // Ejemplo de uso de la función eleva
    printf("Ingrese la base y el exponente para elevar un numero: ");
    scanf("%d %d", &base, &exponente);
    printf("El resultado de elevar %d a la %d es: %d\n", base, exponente, eleva(base, exponente));
    
    return 0;
}
