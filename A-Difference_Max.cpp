#include <iostream>
#include <vector>
using namespace std;

int main(){
    int a, b, c, d;
    cin >> a >> b;
    cin >> c >> d;
    vector<int> C = {a - c, a - d, b - c, b - d};
    int ans = -10000000;

    for (int i = 0; i < 4; i++){
        if (ans < C.at(i)){
            ans = C.at(i);
        }
    }
    cout << ans << endl;

}