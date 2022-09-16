#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>
#include <algorithm>
#include <limits>
using namespace std;

int n, m, c;
vector<int> arrivalTimes;
vector<vector<int>> memo;

int bus(int cow_i, int busesLeft) {
	//cerr << cow_i << ' ' <<busesLeft << "\n";
	if (memo[cow_i][busesLeft-1] >= 0) {
		return memo[cow_i][busesLeft];
	}
	// cerr << "arrival time and cow_i " << arrivalTimes.size() << " " << cow_i << "\n";
	//cerr << "here";
	if (cow_i == arrivalTimes.size()) {
		//cerr << "Cows are taken";
		return 0;
	}
	if (busesLeft == 0) {
		//cerr << "No more buses :(";
		return numeric_limits<int>::max();
	}
	vector<int> busWaitTime;
	int time;
	int minCows = max(1, static_cast<int>(arrivalTimes.size()) - cow_i - c*(busesLeft-1));
    int maxCows = min(c, static_cast<int>(arrivalTimes.size()) - cow_i);
    for (int i = minCows; i <= maxCows; i++){
    	time = max(bus(cow_i+i, busesLeft-1), 
            arrivalTimes[cow_i+i-1] - arrivalTimes[cow_i]);
    	busWaitTime.push_back(time);
    }
    // for(vector<int>::iterator itr = busWaitTime.begin(); itr != busWaitTime.end(); ++itr){
    // 	cerr << *itr << " ";
    // }
    std::vector<int>::iterator result = std::min_element(busWaitTime.begin(), busWaitTime.end());
    time = *result;
    //cerr << time << " ";
    //cerr << time;
    memo[cow_i][busesLeft-1] = time;
    return time;

}

int main() {
    ofstream fout ("convention.out", ios::out);
    ifstream fin ("convention.in", ios::in);
    fin >> n >> m >> c;
    for (int i = 0; i < n+1; i++){
    	memo.push_back({-1});
    	for (int j = 0; j < m-1; j++){
    		memo[i].push_back(-1);
    	}
    }
    
    int time;
    for (int i = 0; i < n; i++) {
    	fin >> time;
    	arrivalTimes.push_back(time);
    }
    sort(arrivalTimes.begin(), arrivalTimes.end());
    time = bus(0, m);
    // for (int i = 0; i < n; i++){
    // 	for (int j = 0; j < m; j++){
    // 		cerr << memo[i][j] << " ";
    // 	}
    // 	cerr << "\n";
    // }
    fout << time;

}