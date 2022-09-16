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
	vector<int> starts(m+1);
	vector<int> ends(m+1);
	vector<int> changes(2*m+1, 0);
	int a, b;
	for(int i = 0; i < n; i++){
		cin >> a >> b;
		starts[a]++;
		ends[b]++;

	}

	int x1, x2, y1, y2;
	for(int i = 0; i <= m; i++){
		x1 = starts[i];
		y1 = ends[i];

		changes[2*i] += x1*x1;
		changes[2*i+1] -= y1*y1;	
		
		for(int j = i+1; j <= m; j++){
			x2 = starts[j];
			y2 = ends[j];

			changes[i+j] += 2*x1*x2;
			changes[i+j+1] -= 2*y1*y2;
			
		}
	}

	for(int i:changes){
		cerr << i << " ";
	}
	ll value = 0;
	for(int i = 0; i < 2*m+1; i++){
		value += changes[i];
		cout << value << "\n";
	}


}