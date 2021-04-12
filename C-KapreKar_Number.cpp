#include <iostream>
#include <vector>
using namespace std;

int digits(int n){
    int digit = 1;
    while(n >= 10){
        n /= 10;
        digit += 1;
    }
    return digit;
}

vector<int> digits_number(int n, int digit, vector<int> nums){
    
    for (int i = 0; i < digit; i ++){
        int t = n % 10;
        nums.at(i) = t;
        n /= 10;
        
    }
    sort(nums.begin(), nums.end());

    return nums;
}

int g1(int n, int digit, vector<int> nums){
    int ans = 0;
    int m = 1;
    for (int i = 0; i < digit - 1; i ++){
        m *= 10;
    }
    for (int i = 0; i < digit; i ++){
        ans += nums.at(digit - i - 1) * m;
        m /= 10;
    }

    return ans;
}

int g2(int n, int digit, vector<int> nums){
    int ans = 0;
    int m = 1;
    for (int i = 0; i < digit - 1; i ++){
        
        m *= 10;
        
        
    }
    for (int i = 0; i < digit; i ++){
        ans += nums.at(i) * m;
        m /= 10;
    
    }
    return ans;
}

int f(int x, int y){
    return x - y;
}

int main(){
    int n, k;
    cin >> n >> k;

    for (int i = 0; i < k; i ++){
        int digit = digits(n);
        
        vector<int> nums(digit);
        nums = digits_number(n, digit, nums);
        
        int x = g1(n, digit, nums);
        int y = g2(n, digit, nums);
        
        n = f(x, y);
    }
    cout << n << endl;
}
