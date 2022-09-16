#include <bits/stdc++.h>
using namespace std;

#define f first
#define s second

int main() {
	int M = 4;
	vector<pair<int,pair<int,int>>> v;
	for (int i = 0; i < M; ++i) {
		int a,b,w; cin >> a >> b >> w;
		v.push_back({w,{a,b}});
	}
	sort(begin(v),end(v));
	for (auto e: v) cout << e.s.f << " " << e.s.s << " " << e.f << "\n";
}