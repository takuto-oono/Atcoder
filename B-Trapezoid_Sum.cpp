#include <iostream>
#include <vector>
using namespace std;

int main(){
    int n;
    cin >> n;
    long long ans;
    for (int i = 0; i < n; i ++){
        long long a, b;
        cin >> a >> b;
        for (int j = a; j < b + 1; j ++){
            ans += j;
        }
    }
    cout << ans << endl;
}

