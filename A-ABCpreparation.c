#include <stdio.h>
main(){
    int A, B, C, D;
    scanf("%d%d%d%d", &A, &B, &C, &D);
    int ans = A;
    if (ans > B){
        ans = B;
    }
    if (ans > C){
        ans = C;
    }
    if (ans > D){
        ans = D;
    }
    printf("%d", ans);
}

