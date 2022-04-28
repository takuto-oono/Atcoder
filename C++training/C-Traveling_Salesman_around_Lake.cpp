#include <iostream>
#include <vector>
using namespace std;

int chmax(int x, int y){
    return max(x, y);
}

int main(){
    int k, n;
    cin >> k >> n;
    vector<int> A(n);
    for (int i = 0; i < n; i ++) cin >> A.at(i);
    vector<int> B(n);
    for (int i = 0; i < n - 1; i ++){
        B.at(i) = A.at(i + 1) - A.at(i);
    }
    B.at(n - 1) = k - A.at(n - 1) + A.at(0);
    int B_max = 0;
    for (int i = 0; i < n; i ++){
        B_max = chmax(B_max, B.at(i));
    }
    for (int i = 0; i < n; i ++){
        if (B.at(i) == B_max){
            B.at(i) = 0;
            break;
        }
    }

    int ans = 0;
    for (int i = 0; i < n; i ++){
        ans += B.at(i);
    }
    cout << ans << endl;
}

