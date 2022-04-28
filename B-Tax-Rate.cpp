#include <iostream>
#include <stdlib.h>
using namespace std;

int main(){
    int n;
    cin >> n;
    int x = n / 2;
    
    double tax = 1.08;
    for (int i = x; i < n + 1; i++){
        int y = i * tax;
        
        if (y == n){
            cout << i << endl;

            exit(0);
            
        }
    }
    cout << ":(" << endl;
    
}
