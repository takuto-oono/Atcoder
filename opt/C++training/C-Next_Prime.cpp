#include <iostream>
using namespace std;

int main(){
    long long x;
    cin >> x;
    long long max_num = 10000000;

    for (int i = 0; i < max_num; i ++){
        int co = 0;
        for (int j = 2; j < i + x; j ++){
            if ((x + i) % j == 0){
                co += 1;
            }    
        }
        if (co == 0){
            cout << x + i << endl;
            exit(0);
        }
    }
}