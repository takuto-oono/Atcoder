#include <iostream>

using namespace std;

int main(){
    int a, b;
    cin >> a >> b;
    int x;
    if (b == 100){
        x = a * 1000 + b;
    }else if (b >= 1 && b <= 9){
        x = a * 10 + b;
    }else{
        x = a * 100 + b;
    }
    int ans = 0;
    for (int i = 0; i < x + 1; i ++){
        if (i * i == x){
            ans = 1;
        }
    }
    if (ans == 0){
        cout << "No" << endl;
    }else{
        cout << "Yes" << endl;
    }

}
