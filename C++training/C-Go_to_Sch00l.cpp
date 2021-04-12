#include <iostream>
#include <vector>
using namespace std;

int main(){
    int n;
    cin >> n;
    vector<int> A(n);
    for (int i = 0; i < n; i ++) cin >> A.at(i);

    for (int i = 0; i < n; i ++){
        for (int j = 0; j < n; j ++){
            if (A.at(j) == i + 1 && i < n - 1){
                cout << j + 1;
                cout << " ";
                
                break;
            }else if(A.at(j) == i + 1 && i == n - 1){
                cout << j + 1 << endl;
                break;
            }
        }
    }
}

