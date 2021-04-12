#include <iostream>
#include <vector>
using namespace std;

int main(){
    int n, s, d;
    cin >> n >> s >> d;
    int ans = 0;

    for (int i = 0; i < n; i ++){
        int x, y;
        cin >> x >> y;
        if (x < s && y > d){
            ans += y;
        }
    }
    if (ans == 0){
        cout << "No" << endl;
    }else{
        cout << "Yes" << endl;
    }
}