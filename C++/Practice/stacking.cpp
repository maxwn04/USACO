#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <iterator>
#include <cmath>


#define pii pair<int, int>;
#define vi vector<int>;
#define mii map<int, int>
#define sp << " " <<
#define lin << "\n";
#define ll long long
#define loops(a,b) for(int i = a; i < b; i++)

using namespace std;
int n, k;

int main(){
	ifstream fin ("stacking.in");
	ofstream fout ("stacking.out");
	fin >> n >> k;
	mii instructions;
	mii sizes;
	int a, b;
	loops(0, k){
		cin >> a >> b;
		if (instructions.find(a) == instructions.end() ) {
  			instructions[a] = 0;
  		}
  		if (instructions.find(b+1) == instructions.end() ) {
  			instructions[b+1] = 0;
  		}
		instructions[a] += 1;
		instructions[b+1] -= 1;
	}

	int at = 0;
	int place = 0;
	
	for (map<int, int>::iterator itr = instructions.begin(); itr != instructions.end(); ++itr){
		//cout << place sp 
		sizes[place] += itr->first - at;
		place += itr->second;
		at = itr->first;
	}

	int value = ceil(n/2);
	int ans;
	for (map<int, int>::iterator itr = sizes.begin(); itr != sizes.end(); ++itr){
		//cout << itr->first sp itr->second sp value lin
		value -= itr->second;
		if(value <= 0){
			ans = itr->first;
			break;
		}
	}
	fout << ans;
}