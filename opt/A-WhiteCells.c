#include <stdio.h>

main(){
    int H, W, h, w;
    scanf("%d %d %d %d", &H, &W, &h, &w);
    int ans;
    ans = (H - h) * (W - w);
    printf("%d", ans);
}