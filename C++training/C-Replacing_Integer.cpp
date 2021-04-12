#include <iostream>
using namespace std;




int main(){
    long long n, k;
    cin >> n >> k;
    int l = n % k;
    int m;
    m = abs(n - k);
    int ans;
    if (m <= l){
        ans = m;
    }else{
        ans = l;
    }
    cout << ans << endl;
}


