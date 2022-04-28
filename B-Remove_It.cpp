#include <iostream>
#include <vector>
using namespace std;

int main(){
    int n, x;
    cin >> n >> x;
    vector<int> A(n);
    for (int i = 0; i < n; i ++) cin >> A.at(i);

    for (int i = 0; i < n; i ++){
        if (i == n - 1){
            if (A.at(i) == x){
                cout << endl;
            }else{
                cout << A.at(i) << endl;
            }
        }else{
            if (A.at(i) != x){
                cout << A.at(i);
                cout << " ";
            }
        }
    }
}