#include <stdio.h>

maint(){
    char b;
    scanf("%c", &b);
    if (b == 'A'){
        printf('T');
    } else if (b == 'T'){
        printf('A');
    } else if (b == 'G'){
        printf('C');
    }else {
        printf('G');
    }
}

