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


int t, n, m, k, a, b;
vi nodeComponent;
vi mostrecent;
vector<int> closest;
vector<vi> adj_list;

void getComponent(int node, int component)
{

	/*cerr << "hi" << node sp component lin;
	for(int i:adj_list[node]){
		cerr << i lin;
	}*/
	nodeComponent[node] = component;
	for(int i:adj_list[node]){
		if(nodeComponent[i] < 0){
			getComponent(i, component);
		}
	}
}

int index(int numcomponents, int component1, int component2){
	//cerr << numcomponents*(numcomponents-1)/2 sp (numcomponents-component1)*((numcomponents-component1-1))/2 sp component2-component1-1;
	int a =  numcomponents*(numcomponents-1)/2;
	int b = (numcomponents-component1)*((numcomponents-component1-1))/2;
	int c = component2-component1-1;
	return a - b + c;
}

int main(){
	cin >> t;

	for(int i = 0; i < t; i++){
		//cerr << "trial " << i lin;
		cin >> n >> m;
		nodeComponent.clear();
		nodeComponent.resize(n, -1);
		adj_list.clear();
		adj_list.resize(n);
		for(int j = 0; j < m; j++){
			cin >> a >> b;
			adj_list[a-1].push_back(b-1);
			adj_list[b-1].push_back(a-1);
		}
		/*for (int j = 0; j < n; j++){
			for (int k = 0; k < adj_list[j].size(); k++){
				cerr << adj_list[j][k] << " ";
			}
			cerr lin;
		}
		cerr lin;*/
		/*for(auto x:adj_list){
			for(int y:x){
				cerr << y << " ";
			}
			cerr lin;
		}*/

		int numcomponents = 0;
		for(int j = 0; j < n; ++j){
			if(nodeComponent[j] < 0){
				getComponent(j, numcomponents);
				numcomponents ++;
			}
		}

		nodeComponent.clear();
		adj_list.clear();

		/*for(int j:nodeComponent){
			cerr << i lin;
		}*/

		closest.clear();
		closest.resize(numcomponents*(numcomponents-1)/2);
		mostrecent.clear();
		mostrecent.resize(numcomponents, -1);
		

		// j is the node number we're comparing
		// nodeComponent[j] is the component # of j
		// mostrecent[nodeComponent[j]-1] = j sets the most recent time we found this component to j
		// k is the component we are comparing to

		for(int j = 0; j < n; j++){
			//cerr << j+1 << " node: ";
			mostrecent[nodeComponent[j]] = j;
			//cerr << nodeComponent[j] << " k:";
			for(int k = 0; k < numcomponents; k++){
				//cerr << k+1 << " ";
				if(mostrecent[k] >= 0 && k != nodeComponent[j]){
					int dist = j - mostrecent[k];
					//cerr << "(dist: " << dist << ") ";
					if(dist < closest[index(numcomponents, nodeComponent[j], k)]){
						closest[index(numcomponents, nodeComponent[j], k)] = dist;
						// cerr << j sp nodeComponent[j] sp k sp closest[nodeComponent[j]][k] lin;
					}
				}
			}
			//cerr lin;
		}
		//cerr << "here!";
		/*for(int j = 0; j < numcomponents; j++){
			for(int k = 0; k < numcomponents; k++){
				cerr << closest[j][k] << " ";

			}
			cerr lin;
		}*/

		/*for(int k:nodeComponent){
			cerr << k << " ";
		}*/
		//cerr << "component num " << nodeComponent[n-1];
		//cerr << "dist " << closest[0][1];
		ll costPair, leastCost;
		if(nodeComponent[n-1] == 0){
			leastCost = 0;
		}else{
			leastCost = pow(closest[index(numcomponents, 0, nodeComponent[n-1])], 2);
			//cerr << leastCost lin;
			for(int j = 1; j < numcomponents; j++){
				if(j != nodeComponent[n-1]){
					costPair = pow(closest[index(numcomponents, 0, j)], 2) + pow(closest[index(numcomponents, j, nodeComponent[n-1])], 2);
					//cerr << j sp costPair lin;
					if (costPair < leastCost){
						leastCost = costPair;
						//cerr << "least cost " << leastCost lin;
					}
				}
			}
		}
		cout << leastCost lin;
		closest.clear();
		mostrecent.clear();
		
	}

}