#include <iostream>
#include <string>
#include <math.h>
using namespace std;

int main(){
    int a, b;
    cin >> a >> b;
    int x = 0, y = 0;
    for (int i = 0; i < 3; i++){
        x += a % 10;
        a = floor(a / 10);
        y += b % 10;
        b = floor(b / 10);
    }

    int ans;
    if (x >= y){
        ans = x;
    }else{
        ans = y;
    }
    cout << ans << endl;
}
    

