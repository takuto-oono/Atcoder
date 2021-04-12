#include <iostream>
#include <vector>
using namespace std;

int main(){
    int k;
    cin >> k;
    long long ans = 0;

    for (int i = 1; i <= k; i ++){
        for (int j = 1; i * j <= k; j ++){
            ans += k /(i * j);
        }
    }
    cout << ans << endl;
    
}
