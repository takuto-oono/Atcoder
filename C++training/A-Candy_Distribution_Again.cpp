#include <iostream>
#include <vector>
using namespace std;

int main(){
    int n;
    long long x;
    cin >> n >> x;
    vector<int> A(n);
    for (int i = 0; i < n; i ++) cin >> A.at(i);
    sort(A.begin(),A.end());
    int ans = 0;

    for (int i = 0; i < n; i ++){
        if (i == n - 1){
            if (A.at(i) == x){
                ans += 1;
            }
        }else if (A.at(i) <= x){
            ans += 1;
            x -= A.at(i);
        }else{
            break;
        }
    }
    cout << ans << endl;
}