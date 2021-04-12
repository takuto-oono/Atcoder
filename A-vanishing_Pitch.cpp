#include <iostream>
#include <string>
using namespace std;

int main(){
    int v, t, s, d;
    cin >> v >> t >> s >> d;
    int dis_t, dis_s;
    dis_t = v * t;
    dis_s = s * v;
    if (dis_t <= d && dis_s >= d){
        cout << "No" << endl;
    }else{
        cout << "Yes" << endl;
    }
}
