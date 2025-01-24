/*Este código sirve para saber el IMC de las personas
Chong Santiago Hungman Emmanuel
07/06/2024*/

#include <stdio.h>

void calculate_bmi() {
    float weight, height, bmi;
    int age;
    char response;

    do {
        // Request data from the user
        printf("Enter your weight in kilograms: ");
        scanf("%f", &weight);

        printf("Enter your height in meters: ");
        scanf("%f", &height);

        printf("Enter your age in years: ");
        scanf("%d", &age);

        // Calculate BMI
        bmi = weight / (height * height);

        // Determine risk condition according to BMI
        if (bmi < 18.5) {
            printf("Your BMI is: %.2f\n", bmi);
            printf("Risk condition for coronary diseases: Underweight\n");
        } else if (bmi >= 18.5 && bmi < 24.9) {
            printf("Your BMI is: %.2f\n", bmi);
            printf("Risk condition for coronary diseases: Normal weight\n");
        } else if (bmi >= 25 && bmi < 29.9) {
            printf("Your BMI is: %.2f\n", bmi);
            printf("Risk condition for coronary diseases: Overweight\n");
        } else {
            printf("Your BMI is: %.2f\n", bmi);
            printf("Risk condition for coronary diseases: Obesity\n");
        }

        // Ask if the user wants to repeat the calculation
        printf("Do you want to perform another calculation? (y/n): ");
        scanf(" %c", &response);

    } while (response == 'y' || response == 'Y');
}

int main() {
    calculate_bmi();
    return 0;
}