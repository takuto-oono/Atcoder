#include <iostream>
#include <vector>
using namespace std;

int main(){
    vector<vector<int> > A(3, vector<int>(3));
    for (int i = 0; i < 3; i ++){
        for (int j = 0; j < 3; j ++){
            cin >> A.at(i).at(j);
        }
    }
    int n;
    cin >> n;
    vector<int> B(n);
    for (int i = 0; i < n; i ++) cin >> B.at(i);

    for (int i = 0; i < n; i ++){
        for (int j = 0; j < 3; j ++){
            for (int k = 0; k < 3; k ++){
                if (A.at(j).at(k) == B.at(i)){
                    A.at(j).at(k) = 0;
                }
            }
        }
    }

    int ans = 0;
    for (int i = 0; i < 3; i ++){
        if (A.at(i).at(0) == 0 && A.at(i).at(1) == 0 && A.at(i).at(2) == 0){
            ans += 1;
        }
        if (A.at(0).at(i) == 0 && A.at(1).at(i) == 0 && A.at(2).at(i) == 0){
            ans += 1;
        }
        if (A.at(0).at(0) == 0 && A.at(1).at(1) == 0 && A.at(2).at(2) == 0){
            ans += 1;
        }
        if (A.at(0).at(2) == 0 && A.at(1).at(1) == 0 && A.at(2).at(0) == 0){
            ans += 1;
        }
    }
    if (ans == 0){
        cout << "No" << endl;
    }else{
        cout << "Yes" << endl;
    }
}
        