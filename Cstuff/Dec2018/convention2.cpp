#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>
#include <algorithm>
#include <limits>
using namespace std;
 
int n,m,c;
vector<int> arrivalTimes;

bool tWork(int t){
	int buses = m-1;
	int start = arrivalTimes[0];
	int cowsOn = 0;
	for (int i = 0; i < n; i++) {
		if (cowsOn == c) {
			//cerr << arrivalTimes[i] << " " << buses << "\n";
			cowsOn = 0;
			buses--;
			start = arrivalTimes[i];

		}
		if (arrivalTimes[i] - start > t){
			//cerr << arrivalTimes[i] << " " << buses << "\n";
			cowsOn = 0;
			buses--;
			start = arrivalTimes[i];
		}
		cowsOn++;
		if (buses < 0) {
			return false;
		}
	}
	return true;
}
 
int search(int low, int high){
	int mid = (low + high)/2;
	if (tWork(mid)){
		if (!tWork(mid-1)){
			return mid;
		}
		return search(low, mid);
	} else {
		return search(mid+1, high);
	}
	return 0;
}

int main()
{
	ofstream fout ("convention.out", ios::out);
    ifstream fin ("convention.in", ios::in);
    fin >> n >> m >> c;
    int time;
    for (int i = 0; i < n; i++) {
    	fin >> time;
    	arrivalTimes.push_back(time);
    }
	sort(arrivalTimes.begin(), arrivalTimes.end());
	int a = search(0, 1000000000);
	fout << a;

}