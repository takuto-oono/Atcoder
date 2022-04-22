#include <iostream>
#include <string>
using namespace std;

int main(){
    int a, b, c;
    cin >> a >> b >> c;
    int x = a - b;

    if (c == 0){
        if (x >= 1){
            cout << "Takahashi" << endl;
        }else{
            cout << "Aoki" << endl;
        }
    }else{
        if (x >= 0){
            cout << "Takahashi" << endl;
        }else{
            cout << "Aoki" << endl;
        }
    }
}
