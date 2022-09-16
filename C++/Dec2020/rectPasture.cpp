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
typedef map<int, vector<int>> iToList;
iToList xToCow, yToCow, cowToCoord;
int cows;
long long ans;

int main(){
	//ifstream cin ("test.in");
	//ofstream cout ("test.out");
	cin >> n;
	ans = pow(2, n)-3;
	cout << ans;

}