#include <iostream>
#include <vector>
using namespace std;

int even(int x){
    return 3 * x + 1;
}

int odd(int x){
    return x / 2;
}

int main(){
    int s;
    cin >> s;
    int co_max = 1000000;
    vector<int> check(co_max);
    check.at(0) = s;
    for (int i = 0; i < co_max; i ++){
        if (s % 2 == 0){
            s = odd(s);
            check.at(i + 1) = s;
        }else if (s % 2 == 1){
            s = even(s);
            check.at(i + 1) = s;
        }
        
        for (int j = 0; j < i + 1; j ++){
            
            if (check.at(j) == s){
                cout << i + 2 << endl;
                
                exit(0);
            }
        }
    }
}
                
