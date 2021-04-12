#include <stdio.h>
main(){
    int x;
    scanf("%d", &x);
    int ans;
    if (x >= 0){
        ans = x;
    }else{
        ans = 0;
    }
    printf("%d", ans);
}