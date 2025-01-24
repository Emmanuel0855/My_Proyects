/*Size of vairables
Chong Santiago Hungman Emmanuel
3/06/2024
*/ 

#include <stdio.h>

int main() {
    printf("Size of int: %zu bytes (%zu bits)\n", sizeof(int), sizeof(int) * 8);
    printf("Size of float: %zu bytes (%zu bits)\n", sizeof(float), sizeof(float) * 8);
    printf("Size of char: %zu bytes (%zu bits)\n", sizeof(char), sizeof(char) * 8);
    printf("Size of double: %zu bytes (%zu bits)\n", sizeof(double), sizeof(double) * 8);
    printf("Size of unsigned short int: %zu bytes (%zu bits)\n", sizeof(unsigned short int), sizeof(unsigned short int) * 8);
    printf("Size of short int: %zu bytes (%zu bits)\n", sizeof(short int), sizeof(short int) * 8);
	printf("Size of unsigned int: %zu bytes (%zu bits)\n", sizeof(unsigned int), sizeof(unsigned int)*8);
	printf("Size of long int: %zu bytes (%zu bits)\n", sizeof(long int), sizeof(long int)*8);
	printf("Size of unsigned long int: %zu bytes (%zu bits)\n", sizeof(unsigned long int), sizeof(unsigned long int)*8);
	printf("Size of long long int: %zu bytes (%zu bits)\n", sizeof(long long int), sizeof(long long int)*8);
	printf("Size of unsigned long long int: %zu bytes (%zu bits)\n", sizeof(unsigned long long int), sizeof(unsigned long long int)*8);
	printf("Size of signed char: %zu bytes (%zu bits)\n", sizeof(signed char), sizeof(signed char) * 8);
return 0;
}