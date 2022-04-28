#include <stdio.h>

main(){
    int a, b;
    scanf("%d%d", &a, &b);
    int x = 0, y = 0;
    for (int i = 0; i < 3; i ++){
        x += a % 10;
        a = float(a / 10);
        y += b % 10;
        b = float(b / 10);
    }

    int ans;
    if (x >= y){
        ans = x;
    }else{
        ans = y;
    }
    printf("%d\n", ans);
}



