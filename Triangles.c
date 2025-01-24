/*Calcuate the area of 2 triangles and print the smallest*/
#include <stdio.h>

// Function to calculate the area of a triangle
float calculateArea(float base, float height) {
    return 0.5 * base * height;
}

int main() {
    float base1, height1, base2, height2;
    float area1, area2;

    // Input base and height for the first triangle
    printf("Enter the base and height of the first triangle: ");
    scanf("%f %f", &base1, &height1);

    // Input base and height for the second triangle
    printf("Enter the base and height of the second triangle: ");
    scanf("%f %f", &base2, &height2);

    // Calculate the area of the first triangle
    area1 = calculateArea(base1, height1);

    // Calculate the area of the second triangle
    area2 = calculateArea(base2, height2);

    // Print the areas
    printf("Area of the first triangle: %.2f\n", area1);
    printf("Area of the second triangle: %.2f\n", area2);

    // Compare the areas and print the smallest one
    if (area1 < area2) {
        printf("The smallest area is: %.2f\n", area1);
    } else if (area2 < area1) {
        printf("The smallest area is: %.2f\n", area2);
    } else {
        printf("Both triangles have the same area: %.2f\n", area1);
    }

    return 0;
}
