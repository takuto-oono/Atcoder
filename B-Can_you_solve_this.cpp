#include <iostream>
#include <vector>
using namespace std;

int main(){
    int n, m, c;
    cin >> n >> m >> c;
    vector<int> B(m);
    for (int i = 0; i < m; i ++) cin >> B.at(i);

    vector<vector<int> > A(n, vector<int>(m));
    for (int i = 0; i < n; i ++){
        for (int j = 0; j < m; j ++){
            cin >> A.at(i).at(j);
        }
    }
    int ans = 0;
    int x = c;

    for (int i = 0; i < n; i ++){
        x = c;
        for (int j = 0; j < m; j ++){
            x += A.at(i).at(j) * B.at(j);
        }
        if (x > 0){
            ans += 1;
        }
    }
    cout << ans << endl;
}