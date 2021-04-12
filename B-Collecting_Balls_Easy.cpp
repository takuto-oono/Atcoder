#include <iostream>
#include <vector>
using namespace std;

int main(){
    int n, k;
    cin >> n >> k;
    vector<int> X(n);
    for (int i = 0; i < n; i ++) cin >> X.at(i);
    int ans = 0;
    for (int i = 0; i < n; i++){
        int a_dis, b_dis;
        a_dis = X.at(i);
        b_dis = abs(X.at(i) - k);
        ans += 2 * min(a_dis, b_dis);
    }
    cout << ans << endl;
}