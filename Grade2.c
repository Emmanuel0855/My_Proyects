/*Create an program that writes the grade corresponding to a grade, according the following criteria
Chong Santiago Hungman Emmanuel
10/06/2024*/

#include <stdio.h>

int main(){
	int Grades;
	printf("Selct Number: "); 
	scanf("%d", &Grades);
	switch (Grades){
	case 10: 
		printf("Honors");
		break;
	case 9:
		printf("Outstanding");
		break;
	case 8: 
		printf("Regular");
		break;
	case 7: 
		printf("pass");
		break;
	case 6:
		printf("Reprobate");
		break;
	}
	return 0;	
}