#include <iostream>
using namespace std;



int judgment(int x, int y, int z){
    if (x % 2 == 0 && y % 2 == 0 && z % 2 == 0){
        return 1;
    }else{
        return 0;
    }
}


int main(){
    int a, b, c;
    cin >> a >> b >> c;
    int ans = 0;
    
    while (judgment(a, b, c) == 1){
        int x = a, y = b, z = c;
        a = (y + z) / 2;
        b = (x + z) / 2;
        c = (x + y) / 2;
        ans += 1;
        if (ans > 100000000){
            ans = -1;
            break;
        }
        

    }
    cout << ans << endl;
}


