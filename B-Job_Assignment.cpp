#include <iostream>
#include <vector>
using namespace std;


int main(){
    int n;
    cin >> n;
    vector<vector<int> > jobs_time(n, vector<int>(2));


    for (int i = 0; i < n; i++){
        for (int j = 0; j < 2; j ++){
            cin >> jobs_time.at(i).at(j);
        }
    }
    int jobs_finish_time = 10000000;

    for (int i = 0; i < n; i ++){
        for (int j = 0; j < n; j ++){
            if (i == j){
                jobs_finish_time = min(jobs_finish_time, (jobs_time.at(i).at(0) + jobs_time.at(j).at(1)));
            }else {
                jobs_finish_time = min(jobs_finish_time, (max(jobs_time.at(i).at(0), jobs_time.at(j).at(1))));
            }
        }
    }
    cout << jobs_finish_time << endl;
}

