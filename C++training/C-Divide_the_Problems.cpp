#include <iostream>
#include <vector>
using namespace std;


int main(){
    int n;
    cin >> n;
    vector<int> D(n);
    for (int i = 0; i < n; i ++) cin >> D.at(i);
    sort(D.begin(),D.end());

    int half = n / 2;
    int ans = D.at(half) - D.at(half - 1);

    cout << ans << endl;
    
}