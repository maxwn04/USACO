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
int n, a, b, edges, ans = 0;
vector<vector<int>> adjList;
vector<int> here;

int infectAdjacent(int edges){
	int a = ceil(log2(edges+1)) + edges;
	return a;
}

/*int spread(int at){
	int mustSpreadTo = 0;
	here[at-1] = 1;
	for(int i = 0; i < adjList[at-1].size(); i++){
		int nextBarn = adjList[at-1][i];
		if(here[nextBarn] == 0){
			spread(nextBarn);

		}
	}
	return 1;
}*/

int main(){
	int cur;
	//ifstream cin ("test.in");
	//ofstream cout ("test.out");
	cin >> n;
	for(int i = 0; i < n; i++){
		adjList.push_back({});
		here.push_back(0);
	}
	for(int i = 0; i < n-1; i++){
		cin >> a >> b;
		adjList[a-1].push_back(b);
		adjList[b-1].push_back(a);
	}
	for(int i = 0; i < n; i++){
		edges = adjList[i].size();
		//cerr << edges << "\n";
		int minus = 1;
		if(i == 0){
			minus = 0;
		}
		cur = infectAdjacent(edges-minus);
		//cerr << cur << "\n";
		ans += cur;
	}
	cout << ans;
}