#include <iostream>
#include <vector>

using namespace std;

int main(){
    int n, k;
    cin >> n >> k;
    vector<vector<int> > T(n, vector<int>(n));

    for (int i = 0; i < n; i ++){
        for (int j = 0; j < n; j ++){
            cin >> T.at(i).at(j);
        }
    }



}