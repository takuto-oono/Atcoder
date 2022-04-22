#include <iostream>
#include <vector>
using namespace std;

int main(){
    int n;
    cin >> n;
    vector<vector<int> > data(n, vector<int>(2));
    for (int i = 0; i < n; i ++){
        for (int j = 0; j < 2; j ++){
            cin >> data.at(i).at(j);
        }
    }
    int ans = 0;
    for (int i = 0; i < n; i++){
        for (int j = i + 1; j < n; j ++){
            double x_dif, y_dif;
            double inclination;
            x_dif = data.at(i).at(0) - data.at(j).at(0);
            y_dif = data.at(i).at(1) - data.at(j).at(1);
            inclination = y_dif / x_dif;
            
            if (inclination >= -1 && inclination <= 1){
                
                ans += 1;
            }
        }
    }
    cout << ans << endl;
}
