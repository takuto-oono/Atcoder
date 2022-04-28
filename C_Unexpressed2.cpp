#include <iostream>
#include <vector>
#include <set>
using namespace std;

int main(){
    long long n;
    cin >> n;
    vector<long long> memo(n);
    long long n_sqrt, cu, ans;
    n_sqrt = sqrt(n);
    
    for (int i = 0; i < n; i ++){
        memo.at(i) = i + 1;
    }

    for (int i = 2; i < n_sqrt + 1; i ++){
        cu = i;
        while(cu * i <= n){
            cu *= i;
            memo[cu- 1] = 0;
            
        }
    }
    ans = 0;
    for (int i = 0; i < n; i ++){
        if (memo[i] != 0){
            ans += 1;
        }

    }
    cout << ans << endl;
}