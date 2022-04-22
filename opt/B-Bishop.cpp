#include <iostream>
#include <math.h>
using namespace std;

int main(){
    long long w, h, ans;
    cin >> h >> w;
    if (min(h, w) == 1){
        ans = 1;
    
    }else if (w % 2 == 1 && h % 2 == 1){
        ans = h * w / 2 + 1;
    }else{
        ans = h * w / 2;
    }
    cout << ans << endl;
}
