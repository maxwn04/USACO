#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <iterator>

using namespace std;
int n, num, bigOne = 0, bigTwo = 0;
vector<vector<int>> grid;
vector<vector<string>> memo;
typedef set<pair<int, int>> component;
typedef vector<component> cList;
map<int, cList> idToCs;
map<string, int> componentSize;


int region(int x, int y, int num, int cnum){
	idToCs[num][cnum].insert((x, y));
	memo[x][y] = to_String(num) + ' ' + to_String(cnum);
	int area = 1;
	if (x+1 < n && memo[x+1][y] == 0 && grid[x+1][y] == num){
		area += region(x+1, y, num);
	}
	if (x-1 >= 0 && [x-1][y] == 0 && grid[x-1][y] == num){
		area += region(x-1, y, num);
	}
	if (y+1 < n && memo[x][y+1] == 0 && grid[x][y+1] == num){
		area += region(x, y+1, num);
	}
	if (y-1 >= 0 && memo[x][y-1] == 0 && grid[x][y-1] == num){
		area += region(x, y-1, num);
	}
	return area; 
}

int regionTwo(int x, int y, int num1, int num2){
	int times = num1 * num2;
	memo[x][y] = times;
	int area = 1;
	if (x+1 < n && memo[x+1][y] != times && (grid[x+1][y] == num1 || grid[x+1][y] == num2)){
		area += regionTwo(x+1, y, num1, num2);
	}
	if (x-1 >= 0 && memo[x-1][y] != times && (grid[x-1][y] == num1 || grid[x-1][y] == num2)){
		area += regionTwo(x-1, y, num1, num2);
	}
	if (y+1 < n && memo[x][y+1] != times && (grid[x][y+1] == num1 || grid[x][y+1] == num2)){
		area += regionTwo(x, y+1, num1, num2);
	}
	if (y-1 >= 0 && memo[x][y-1] != times && (grid[x][y-1] == num1 || grid[x][y-1] == num2)){
		area += regionTwo(x, y-1, num1, num2);
	}
	return area; 
}

component neigh(pair<int, int> coord, int num){

	if (x+1 < n && memo[x+1][y] == 0 && grid[x+1][y] == num){
		memo[x+1][y]
	}
	if (x-1 >= 0 && [x-1][y] == 0 && grid[x-1][y] == num){
		area += region(x-1, y, num);
	}
	if (y+1 < n && memo[x][y+1] == 0 && grid[x][y+1] == num){
		area += region(x, y+1, num);
	}
	if (y-1 >= 0 && memo[x][y-1] == 0 && grid[x][y-1] == num){
		area += region(x, y-1, num);
	}
}

int main(){
    ifstream fin ("input.in");
	ofstream fout ("output.out");
	fin >> n;
	for(int i = 0; i < n; i++){
		grid.push_back({});
		memo.push_back({});
		for(int j = 0; j < n; j++){
			fin >> num;
			if (idToCs.find(num) == idToCs.end()){
				idToCs[num]= {};
			}
			grid[i].push_back(num);
			memo[i].push_back("0");
		}
	}
	int highest = 0;
	int regionArea;
	for(int x = 0; x < n; x++){
		for(int y = 0; y < n; y++){
			if (memo[x][y] == "0"){
				idToCs[grid[x][y]].push_back({})
				regionArea = region(x, y, grid[x][y], idToCs[grid[x][y]].size()-1);
			}
			if (regionArea > highest){
				highest = regionArea;
			}
		}
	}
	for(map<int, cList>::iterator itr = idToCs.begin(); itr != idToCs.end(), ++itr){
		int a = itr -> first;
		// may not work. add marker
		for(map<int, cList>::iterator jtr = itr.next(); jtr != idToCs.end(), ++jtr){
			int b = jtr -> first;
			for(i = 0; i < itr->second.size(); i++){
				for(j = 0; j < jtr -> second.size(); j++){
					for(int k = 0; k < itr->second[i]){
						pair<int, int> coord = itr->second[i][k];
					}
				}
			}
		}
	}
	// fout << highest << "\n";
	// highest = 0;
	// for(int i = 1; i < 1000; i++){
	// 	for(int j = i+1; j < 100; j++){
	// 		for(int x = 0; x < n; x++){
	// 			for(int y = 0; y < n; y++){
	// 				if((grid[x][y] == i || grid[x][y] == j) && !(memo[x][y] == i*j)){
	// 					regionArea = regionTwo(x, y, i, j);
	// 					//cerr << i << " " << j << " " << regionArea << "\n";
	// 					if (regionArea > highest){
	// 						highest = regionArea;
	// 					}
	// 				}
	// 			}
	// 		}
	// 	}
	// }
	fout << highest << "\n";
}