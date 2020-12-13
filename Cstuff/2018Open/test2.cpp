#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
    ofstream fout ("output.out", ios::out);
    ifstream fin ("input.in", ios::in);
    int a, b;
    fin >> a >> b;
    fout << a+b << endl;
    return 0;
}