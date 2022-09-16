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
int n, q;
#define vi vector<int>
#define pii pair<int, int>
#define space << " " <<
#define lin << "\n";
#define loops(n) for(int i = 0; i < n; i++)

int main(){
	cin >> n >> q;
	vi a;
	int num;
	for(int i = 0; i < n; i++){
		cin >> num;
		a.push_back(num);
	}
	vector<pii> ranges;
	int x, y;
	for(int i = 0; i < q; i++){
		cin >> x >> y;
		ranges.push_back(make_pair(x, y));
	}

	vi sums;
	int sum = 0;
	sums.push_back(0);
	for (int i = 0; i < n; i++){
		sum += a[i];
		sums.push_back(sum);
	}

	vi ans;
	for (int i = 0; i < q; i++){
		// cout << i space sums[ranges[i].second] space sums[ranges[i].first] lin;
		ans.push_back(sums[ranges[i].second] - sums[ranges[i].first]);
	}

	loops(n + 1){
		cout << sums[i] lin;
	}

	// loops(q){
	// 	cout << ans[i] lin;
	// }

}
