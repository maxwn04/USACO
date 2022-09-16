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
int n, b;
vector<pair<int, int>> boots;

int main(){
	ifstream fin ("snowboots.in");
	ofstream fout ("snowboots.out");
	fin >> n >> b;
	int a;
	vector<int> path;
	for(int i = 0; i < n; i++){
		fin >> a;
		path.push_back(a);
	}
	for(int i = 0; i < 250; i++){
		path.push_back(0);
	}
	int length, depth;
	for(int i = 0; i < b; i++){
		fin >> depth >> length;
		boots.push_back(pair<int,int>(depth, length));
	}
	int space = 0, bootNumber = 0;
	// for(int i = 0; i < n; i++){
	// 	cerr << path[i] << " ";
	// }
	//cerr << n << "\n";
	while(true){
		depth = boots[bootNumber].first;
		length = boots[bootNumber].second;
		//cerr << depth << "\n";
		if(depth >= path[space]){
			for(int i = length; i > 0; i--){				
				if(space >= n-1){
					break;
				}
				if(depth >= path[space+i]){
					space += i;
					i = length;
				}
			}
			if(space >= n-1){
				break;
			}
		}
		bootNumber +=1;
		
		
	}
	fout << bootNumber;
}