#include <iostream>
#include <vector>
using namespace std;

int main(){
    int n, m, x;
    cin >> n >> m >> x;
    vector<int> A(n);
    for (int i = 0; i < m; i ++) cin >> A.at(i);
    int co_low = 0, co_higt = 0;

    for (int i = 0; i < m; i ++){
        if (A.at(i) < x){
            co_low += 1;
        }else if (A.at(i) > x){
            co_higt += 1;
        }
    }
    int ans = min(co_higt, co_low);
    cout << ans << endl;
}