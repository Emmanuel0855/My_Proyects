/*Desarrolla un programa que implemente una función para obtener el índice de positividad en porcentaje, la cantidad de días entre 150 y 200 contagios, tasa de letalidad en porcentaje, el usuario puede ingresar los siguientes contagios por día y almacenarlos
3,000 pruebas de covid dieron los resultados, Lunes 22/ 110, Martes 23/ 188, Miércoles 24/ 182, Jueves 25/ 150, Viernes 26/ 102, Sábado 27/ 230
Dentro de este periódo se registraron 130 fallecimientos
Chong Santiago Hungman Emmanuel 
29/07/2024*/

#include <stdio.h>

struct DatosDia {
    char fecha[20];
    int contagios;
};

int contarDiasEntre150y200(struct DatosDia datos[], int numDias) {
    int contador = 0;

    for (int i = 0; i < numDias; ++i) {
        if (datos[i].contagios >= 150 && datos[i].contagios <= 200) {
            contador++;
        }
    }

    return contador;
}

double calcularTasaLetalidad(int defunciones, int totalContagios) {
    return (double) defunciones / totalContagios * 100;
}

int main() {
    struct DatosDia datos[] = {
        {"Lunes 22", 110},
        {"Martes 23", 188},
        {"Miércoles 24", 182},
        {"Jueves 25", 150},
        {"Viernes 26", 102},
        {"Sábado 27", 230},
		{"Domingo 28", 127},
		{"Lunes 29", 96}
	};

    int numDias = sizeof(datos) / sizeof(datos[0]);
    int defunciones = 130;
    int totalPruebas = 3000;
    int totalContagios = 1185;

	float Positividad = (totalContagios/totalPruebas) * 100;
    int diasEntre150y200 = contarDiasEntre150y200(datos, numDias);
    double tasaLetalidad = calcularTasaLetalidad(defunciones, totalContagios);

    printf("Indice de Positividad: %.2f%%\n", Positividad);
    printf("Dias con contagios entre 150 y 200: %d\n", diasEntre150y200);
    printf("Tasa de Letalidad: %.2f%%\n", tasaLetalidad);

    return 0;
}