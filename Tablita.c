#include <stdio.h>
#include <math.h>

int main() {
    // Open a file to write the data points
    FILE *file = fopen("function_data.txt", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Generate data points for x from -10 to 10
    double x;
    for (x = -10; x <= 10; x += 0.1) {
        double y = pow(x, 2);
        fprintf(file, "%lf %lf\n", x, y);
    }

    // Close the file
    fclose(file);

    printf("Data points written to function_data.txt\n");
    return 0;
}
