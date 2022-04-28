#include <iostream>
#include <vector>
using namespace std;

int main(){
    int n;
    cin >> n;
    long long a, p, x, ans;
    ans = 10000000000;
    for (int i = 0; i < n; i ++){
        cin >> a >> p >> x;
        if (x > a){
            ans = min(ans, p);
        }

    }
    if (ans == 10000000000){
        ans = -1;
    }
    cout << ans << endl;
}