#include <iostream>
#include <string>
using namespace std;

int main(){
    int n, a, b;
    cin >> n >> a >> b;
    char s[n];
    cin >> s;
    int a_count = 0;
    int b_count = 0;

    for (int i = 0; i < n; i ++){
        if (s[i] == 'a'){
            if (a_count + b_count < a + b){
                a_count += 1;
                cout << "Yes" << endl;
            }else{
                cout << "No" << endl;
            }
        }else if(s[i] == 'b'){
            if (b_count < b && a_count + b_count < a + b){
                b_count += 1;
                cout << "Yes" << endl;
            }else{
                cout << "No" << endl;
            }
        }else{
            cout << "No" << endl;
        }
        
    }


}
