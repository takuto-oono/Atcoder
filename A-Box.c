#include <stdio.h>

main(){
    int N, A, B;
    scanf("%d %d %d", &N, &A, &B);
    int ans;
    ans = N - A + B;
    printf("%d\n", ans);
}