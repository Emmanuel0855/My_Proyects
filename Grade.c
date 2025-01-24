/*Create an program that writes the grade corresponding to a grade, according the following criteria
Chong Santiago Hungman Emmanuel
10/06/2024*/

#include <stdio.h>

int main(){
	int Grades;
	printf("Selct Number: "); 
	scanf("%d", &Grades);
	if (Grades==10){
		printf("Honors");
	}
		else if (Grades==9){
		printf("Outstanding");
		}
			else if (Grades==8){ 
			printf("Regular");
			}
				else if (Grades==7){ 
				printf("pass");
				}
					else if (Grades==6){ 
					printf("Reprobate");
					}
	return 0;	
}
