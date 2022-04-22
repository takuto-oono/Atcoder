#include <iostream>
#include <string>
using namespace std;

int main(){
    string C;
    cin >> C;

    if (C.at(0) == C.at(1) && C.at(1) == C.at(2)){
        cout << "Won" << endl;
    }else{
        cout << "Lost" << endl;
    }

}
    