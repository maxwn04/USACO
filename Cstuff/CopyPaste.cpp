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
int n;

int main(){
	ifstream fin ("test.in");
	ofstream fout ("test.out");
	fin >> n;
	fout << n;

}

int inputList(){
	vector<int> a;
	int num;
	for(int i = 0; i < n; i++){
		cin >> num;
		a.push_back(num);
	}
}

int inputGrid(){
	vector<vector<int>> grid;
	int num;
	for(int i = 0; i < n; i++){
		grid.push_back({});
		for(int j = 0; j < n; j++){
			cin >> num;
			grid[i].push_back(num);
		}
	}
}


vector<vector<int>> memo;
int dfs(int x, int y, int num){
	memo[x][y] = 1;
	int area = 1;
	if (x+1 < n && memo[x+1][y] == 0 && grid[x+1][y] == num){
		area += region(x+1, y, num);
	}
	if (x-1 >= 0 && memo[x-1][y] == 0 && grid[x-1][y] == num){
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

int search(int low, int high){
	int mid = (low + high)/2;
	if (work(mid)){
		if (work(mid-1)){
			return mid;
		}
		return search(low, mid);
	} else {
		return search(mid+1, high);
	}
	return 0;
}