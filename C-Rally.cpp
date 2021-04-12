#include <iostream>
#include <vector>
using namespace std;
int chmax(int x, int y){
    return max(x, y);
}
int chmin(int x, int y){
    return min(x, y);
}

int main(){
    int n;
    cin >> n;
    vector<int> X(n);
    for (int i = 0; i < n; i++) cin >> X.at(i);

    int max_value = 0;
    int min_value = 1000;
    for (int i = 0; i < n; i ++){
        max_value = chmax(X.at(i), max_value);
        min_value = chmin(X.at(i), min_value);
    }
    int ans = 1000000000;
    for (int i = min_value; i < max_value + 1; i ++){
        int z = 0;
        for (int j = 0; j < n; j ++){
            z += (X.at(j) - i) * (X.at(j) - i);
        }
        ans = chmin(z, ans);
    }

    cout << ans << endl;

}

