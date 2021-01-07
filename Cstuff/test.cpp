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
	//ifstream fin ("input.in");
	//ofstream fout ("output.out");
	//fin >> n;
	//fout << n;
	map<int, vector<int>> aToB;
	aToB[3] = {5};
	aToB[8] = {9};
	aToB[6] = {9};
	aToB[2] = {1};
	int a = aToB.rbegin()->second[1];
	cerr << a << " ";
}