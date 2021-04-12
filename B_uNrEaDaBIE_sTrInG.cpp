#include <iostream>
#include <string>
using namespace std;

int main(){
    string s;
    cin >> s;
    int len = s.length();
    int co = 0;
    for (int i = 0; i < len; i ++){
        char t = s.at(i);
        t = int(t);
        if (i % 2 == 1){
            if (t >= 65 && t <= 90){
                co += 1;
            }
        } else{
            if (t >= 97 && t <= 122){
                co += 1;
            }
        }
    }
    string ans;
    if (co == len){
        ans = "Yes";
    }else{
        ans = "No";
    }

    cout << ans << endl;
}