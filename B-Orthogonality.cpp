#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main(){
    int n;
    cin >> n;
    vector<int> A(n);
    vector<int> B(n);
    for (int i = 0; i< n;i++) cin >> A.at(i);
    for (int i = 0; i < n; i ++) cin >> B.at(i);

    int inner_product = 0;
    for (int i = 0; i < n; i ++){
        inner_product += A.at(i) * B.at(i);

    }
    if (inner_product == 0){
        cout << "Yes" << endl;
    }else{
        cout << "No" << endl;
    }

}