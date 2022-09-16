#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <iterator>
#include <cmath>

using namespace std;

int n;
#define pii pair<int, int>
#define vi vector<int>
#define mii map<int, int>
#define space << " " <<
#define lin << "\n";
#define loop(a, b) for(int i = a; i < b; i++)


int main(){
	ifstream fin ("div7.in");
	ofstream fout ("div7.out");
	fin >> n;
	int num;
	vi cows;
	loop(0,n){
		fin >> num;
		cows.push_back(num);
	}
	int sum = 0;
	vi first(7,0);
	vi last(7,0);

	loop(0,n){
		sum += cows[i];
		sum = sum % 7;
		if (first[sum] == 0) first[sum] = i+1;
		last[sum] = i+1;
	}
	int ans = 0;
	loop(0,7){
		ans = max(last[i] - first[i], ans);
	}

	if (ans == 0 && first[0] != 0){
		ans = 1;
	}
	// loop(0,7){
	// 	cout << first[i] space last[i] lin;
	// }
	fout << ans;

}