#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <map>
#include <iterator>
#include <cmath>

using namespace std;
#define pii pair<int, int>
#define vi vector<int>
#define mii map<int, int>
#define sp << " " <<
#define lin << "\n"
#define ll long long
#define loops(a, b) for(int i = a; i < b; i++)

int k,m,n;

int main(){
	cin >> k >> m >> n;
	vi cows;
	map<int, ll> grass;
	vi tastyPerCow(2*m, 0);

	int a, b;
	for(int i = 0; i < k; i++){
		cin >> a >> b;
		grass[a] = b;
	}
	for(int i = 0; i < m; i++){
		cin >> a;
		cows.push_back(a);
	}

	sort(cows.begin(), cows.end());
	int cownum = 0;
	map<int, ll>::iterator leadGrass = grass.begin();
	map<int, ll>::iterator trailGrass = grass.begin();
	ll halfTasty = 0;
	ll fullTasty = 0;
	ll bigHalf = 0;



	while(leadGrass->first < cows[0]){
		halfTasty += leadGrass->second;
		++leadGrass;
		if (leadGrass == grass.end()){
			break;
		}
	}
	tastyPerCow[0] = halfTasty;

	trailGrass = leadGrass;
	if(leadGrass != grass.end()){
		for(int i = 0; i < m-1; i++){
			halfTasty = 0;
			bigHalf = 0;
			fullTasty = 0;
			while(leadGrass->first < cows[i+1]){
				if (leadGrass->first - trailGrass->first < ceil((cows[i+1]-cows[i]+1)/2)){
					halfTasty += leadGrass->second;

					if(bigHalf < halfTasty){
						bigHalf = halfTasty;
					}
					
					fullTasty += leadGrass->second;
					++leadGrass;
				} else {
					halfTasty -= trailGrass ->second;
					++trailGrass;
				}
				if (leadGrass == grass.end()){
					break;
				}
			}
			tastyPerCow[2*i+1] = bigHalf;
			tastyPerCow[2*i+2] = (fullTasty-bigHalf);
			trailGrass = leadGrass;

			if (leadGrass == grass.end()){
				break;
			}
		}
	}
	halfTasty = 0;
	for(leadGrass; leadGrass != grass.end(); ++leadGrass){
		halfTasty += leadGrass -> second; 
	}
	tastyPerCow[2*m-1] = halfTasty;

	/*for(auto i : tastyPerCow){
		cerr << i << " ";
	}*/
	cerr lin;

	sort(tastyPerCow.begin(), tastyPerCow.end(), greater<ll>());
	ll ans = 0;
	
	for(int i = 0; i < n && i < tastyPerCow.size(); i++){
		ans += tastyPerCow[i];
	}
	cout << ans;

}