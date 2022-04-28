#include <iostream>
#include <vector>
using namespace std;

int chmax(int x, int y){
    return max(x, y);
}

int main(){
    int n;


    cin >> n;
    vector<int> A(n);
    for (int i = 0; i < n; i ++){
        cin >> A.at(i);
    }
    int player_1 = 0; 
    int player_2 = 0;
    for (int i = 0; i < n; i ++){
        int x = 0; 
        for (int j = 0; j < n; j++){
            x = chmax(x, A.at(j));
        }
        if (i % 2 == 0){
            player_1 += x;
            
        }else if(i % 2 == 1){
            player_2 += x;
            
        }


        for (int j = 0; j < n; j ++){
            if (A.at(j) == x){
                A.at(j) = 0;
                break;
            }
        }
    }
    int ans;
    ans = player_1 - player_2;
    cout << ans << endl;
}


    
