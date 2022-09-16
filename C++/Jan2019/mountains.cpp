#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <map>
#include <string>

using namespace std;

int main(){
	ofstream fout ("sort.out");
    ifstream fin ("sort.in");
    int n;
    fin >> n;
    int a, b;
    map<int, int> startEnd;
    for (int i = 0; i < n; i++){
    	fin >> a >> b;
    	startEnd.insert(pair<int, int>(a, b));

    }

}