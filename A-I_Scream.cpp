#include <iostream>
using namespace std;

int judgment(int a, int b){
    int c = a + b;
    if ((c) >= 15 && b >= 8){
        return 1;
    } else if (c >= 10 && b >= 3){
        return 2;
    } else if (c >= 3){
        return 3;
    } else{
        return 4;
    } 

}

int main(){
    int a, b, ans;
    cin >> a >> b;
    ans = judgment(a, b);
    cout << ans << endl;
    


}