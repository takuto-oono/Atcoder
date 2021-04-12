#include <stdio.h>
int f(a, b, c){
    int x = a * (a + 1) / 2;
    int y = b * (b + 1) / 2;
    int z = c * (c + 1) / 2;
    int ans = (x * y * z) % 998244353;
    return ans;
};
main(){
    int A;
    int B;
    int C;

    scanf("%d%d%d", &A, &B, &C);
    int ans = f(A, B, C);
    printf("%d", ans);
}
    