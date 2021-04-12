#include <iostream>
#include <vector>
using namespace std;

int main(){
    int n;
    cin >> n;
    long long ans = 0;
    long long sum = 0;
    long long sum_squares = 0;
    
    for (int i = 0; i < n; i ++){
        int x;
        cin >> x;
        sum += x;
        sum_squares += x * x;
    }
    
    ans = n * sum_squares - sum * sum;

    cout << ans << endl;
}
