#include <iostream>
#include <string>
using namespace std;
int main(){
    int x, y;
    cin >> x >> y;
    int dif;
    dif = abs(x - y);
    if (dif < 3){
        cout << "Yes" << endl;
    }else{
        cout << "No" << endl;
    }
}
