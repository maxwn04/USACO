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
#define pii pair<int, int>
#define vi vector<int>
#define mii map<int, int>
#define sp << " " <<
#define lin << "\n"
#define ll long long
#define loops(a, b) for(int i = a; i < b; i++)


int t, n, k, a, b;
vi been;
vector<vector<int>> adj_list;

void getComponent(int node, int component)
{
	been[node] = 1;
	for(int i:adj_list[node]){
		if(!been[i]){
			getComponent(i);
		}
	}
}

int main(){
	cin >> t;

	for(int i = 0; i < t; i++){
		//cerr << "trial " << i lin;
		cin >> n >> k;
		been.clear();
		been.resize(n);
		adj_list.clear();
		adj_list.resize(n);
		for(int j = 0; j < k; j++){
			cin >> a >> b;
			adj_list[a-1].push_back(b-1);
			adj_list[b-1].push_back(a-1);
		}

		/*for (int x:been){
			cerr << x << " ";
		}
		cerr lin;*/
		/*for(auto x:adj_list){
			for(int y:x){
				cerr << y << " ";
			}
			cerr lin;
		}*/

		int count = 0;
		for(int j = 0; j < n; ++j){
			if(!been[j]){
				count ++;
				getComponent(j, count);
			}
		}
		cout << count-1 lin;
	}

}