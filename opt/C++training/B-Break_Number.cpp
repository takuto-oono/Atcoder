#include <iostream>
using namespace std;

int chmax(int x, int y){
    return max(x, y);
}

int main(){
    int n;
    cin >> n;
    int ans = 0;
    for (int i = 0; i < n; i ++){
        int x = i + 1;
        int y = 0;
        for (int j = 0; j < 8; j ++){
            if (x % 2 == 0){
                x /= 2;
                y ++;
            }else{
                break;
            }
            
        }
        ans = chmax(ans, y);
    }
    int z = 1;
    for (int i = 0; i < ans; i ++){
        z *= 2;
    }
    cout << z << endl;
}

            


