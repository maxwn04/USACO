#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
using namespace std;

int main()
{
    
    ifstream fin ("input.in", ios::in);
    ofstream fout("output.out", ios::out);
    int n, a;
    fin >> n;
    vector<int> w;
    for (int i = 0; i < n; i++){
        fin >> a;
        w.push_back(a);
    }
    std::sort(w.begin(), w.end());
    int lineSize = 0;
    for (int i = n-1; i >= 0; i--){
        if (w[i] < lineSize){
            break;
        }
        lineSize++;
    }
    //cout << lineSize;
    fout << lineSize << endl;
    return 0;
}