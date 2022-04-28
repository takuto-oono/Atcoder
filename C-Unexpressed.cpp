#include <iostream>
#include <vector>
#include <set>
using namespace std;

int main(){
    long long n;
    cin >> n;
    vector<long long> memo(0);
    long long a, cu;
    a = sqrt(n);
    
    /*cout << a << endl;*/
    for (int i = 2; i < a + 1; i ++){
        cu = i;
        while(cu * i <= n){

            cu *= i;
            memo.push_back(cu);
            
            /*cout << cu << endl;*/
        }
        
    }
    set<long long> S(memo.begin(), memo.end());
    vector<long long> mome(S.begin(), S.end());

    cout << n - mome.size() << endl;
}