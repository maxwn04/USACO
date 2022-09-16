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
int n, m;
#define pii pair<int, int>;
#define vi vector<int>;
#define mii map<int, int>
#define sp << " " <<
#define lin << "\n"
#define ll long long
#define loops(a, b) for(int i = a; i < b; i++)


int main(){
	cin >> n >> m;
	vector<int> starts;
	vector<int> ends;
	vector<int> changes(2*m+1, 0);
	int a, b;
	for(int i = 0; i < n; i++){
		cin >> a >> b;
		starts.push_back(a);
		ends.push_back(b);

	}

	for(int i = 0; i < n; i++){
		changes[2*starts[i]] ++;

		for(int j = i+1; j < n; j++){
			changes[starts[i]+starts[j]] += 2;
		}
	}

	for(int i = 0; i < n; i++){
		changes[2*ends[i]+1] --;
		//cerr << 2*ends[i]+1 << " -1\n";

		for(int j = i+1; j < n; j++){
			//cerr << ends[i]+ends[j]+1 << " -2\n";
			changes[ends[i]+ends[j]+1] -= 2	;
		}
	}

	for(int i:changes){
		cerr << i << " ";
	} 

	int value = 0;
	for(int i = 0; i < 2*m+1; i++){
		value += changes[i];
		cout << value << "\n";
	}


}