#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <map>
#include <iterator>
#include <cmath>

using namespace std;
#define pii pair<int, int>;
#define vi vector<int>;
#define mii map<int, int>
#define sp << " " <<
#define lin << "\n"
#define ll long long
#define loops(a, b) for(int i = a; i < b; i++)

int k,m,n;

int main(){
	cin >> k >> m >> n;
	vector<int> cows;
	map<int, int> grass;
	vector<int> halfTotals(m+1, 0);
	vector<int> fullTotals(m+1, 0);

	int a, b;
	for(int i = 0; i < k; i++){
		cin >> a >> b;
		grass[a] = b;
	}
	for(int i = 0; i < m; i++){
		cin >> a;
		cows.push_back(a);
	}


	int cownum = 0;
	map<int, int>::iterator leadGrass = grass.begin();
	map<int, int>::iterator trailGrass = grass.begin();
	int halfTasty = 0;
	int fullTasty = 0;



	while(leadGrass->first < cows[0]){
		halfTotals[0] += leadGrass->second;
		++leadGrass;
	}

	trailGrass = leadGrass;
	for(int i = 0; i < m-1; i++){
		halfTasty = 0;
		fullTasty = 0;
		while(leadGrass->first < cows[i+1]){
			if (leadGrass->first - trailGrass->first < .5 * (cows[i+1]-cows[i])){
				halfTasty += leadGrass->second;

				if(halfTotals[i+1] < halfTasty){
					halfTotals[i+1] = halfTasty;
				}
				
				fullTasty += leadGrass->second;
				++leadGrass;
			} else {
				halfTasty -= trailGrass ->second;
				++trailGrass;
			}
			fullTotals[i+1] = fullTasty;
			if (leadGrass == grass.end()){
				break;
			}
		}
		trailGrass = leadGrass;
	}
	for(leadGrass; leadGrass != grass.end(); ++leadGrass){
		halfTotals[m] += leadGrass -> second; 
	}

	for(auto i : halfTotals){
		cerr << i << " ";
	}
	cerr lin;
	for(auto i : fullTotals){
		cerr << i << " ";
	}
	cerr lin;

	sort(halfTotals.begin(), halfTotals.end(), greater<int>());
	long long ans = 0;
	
	for(int i = 0; i < min(n, m+1); i++){
		ans += halfTotals[i];
	}
	cout << ans;

}