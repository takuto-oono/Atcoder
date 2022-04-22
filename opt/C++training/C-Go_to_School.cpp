#include <iostream>
#include <vector>
using namespace std;

int main(){
    int n;
    
    cin >> n;
    vector<int> A(n);
    for (int i = 0; i < n; i ++) cin >> A.at(i);
    
    vector<int> ans(n);

    for (int i = 0; i < n; i ++){
        ans.at(A.at(i) - 1) = i + 1;
    }

    for (int i = 0; i < n; i++){
        cout << ans.at(i);
        cout << ' ';
    }
    cout << endl;
}
