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
#define pii pair<int, int>
#define vi vector<int>
#define mii map<int, int>
#define sp << " " <<
#define lin << "\n"
#define ll long long
#define loops(a, b) for(int i = a; i < b; i++)


int main(){
	int k, m, n;
	k = 10;
	m = 5;
	n = rand() % 5 + 2;
	cout << k sp m sp n lin;
	loops(0, k){
		cout << rand() % 30 + 1 sp rand() % 10 + 1 lin;
	}
	loops(0, m){
		cout << rand() % 30 + 1 lin;
	}

}