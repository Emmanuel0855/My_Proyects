/*Code for the pairs numbers for 1 to 100
Chong Santiago Hungman Emmanuel 
17/06/2024*/

#include <stdio.h>

int main() {
    int i;

    for(i = 1; i <= 100; i++) {
        if(i % 2 == 0) {
            printf("%d\n", i);
        }
    }

    return 0;
}

