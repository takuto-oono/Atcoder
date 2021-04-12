#include <iostream>
using namespace std;

int main(){
    int x;
    cin >> x;
    int ans = 0;
    if (x % 100 == 0){
        ans = 100;
    }else{
        int y = (x / 100 + 1) * 100;
        ans = y - x;
    }
    cout << ans << endl;
}