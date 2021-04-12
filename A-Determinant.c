#include <stdio.h>
main(){
    int a, b, c, d;
    scanf("%d%d%d%d", &a, &b, &c, &d);
    int ans;
    ans = a * d - c * b;
    printf("%d", ans);
}

