#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <map>
#include <string>
#include <iterator>

using namespace std;

int main(){
    ifstream fin ("input.in");
	ofstream fout ("output.out");
    int n;
    vector<int> a;
    vector<int> aSorted;
    fin >> n;
    int x;
    map<int, vector<int>> numberToIndex;
    for (int i = 0; i < n; i++){
    	fin >> x;
    	a.push_back(x);
    }
    copy(a.begin(), a.end(), back_inserter(aSorted));
    sort(aSorted.begin(), aSorted.end());
    int moos = 0;
    int sorted = 0;
    int biggest, num, sortedIndex, unsortedIndex;
    for (int i = 0; i < n; i++){
        //cerr << "here";
        numberToIndex.insert(pair<int, vector<int>>(aSorted[i], {i}));
    }
    for (int i = 0; i < n; i++){
        numberToIndex[a[i]].push_back(i);
    }
    for (int i = 0; i < n; i++){
        biggest = 0;
        num = aSorted[i];
        sortedIndex = numberToIndex[a[i]][0];
        unsortedIndex = numberToIndex[a[i]][1];
        if (unsortedIndex > sortedIndex){
            biggest = unsortedIndex - sortedIndex;
        
        }
        //cerr << "biggest: " << biggest << "  i: " << i << "\n";
        if (biggest + 1 > moos) {
            moos = biggest + 1;
        }
    }
    fout << moos;

}