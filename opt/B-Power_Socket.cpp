#include <iostream>
using namespace std;

int main(){
    int ans = 0;
    int a, b;
    cin >> a >> b;
    int x = 1;
    while(x < b){
        x += a - 1;
        ans += 1;

    }
    cout << ans << endl;
}