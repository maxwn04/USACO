#include<iostream>
using namespace std;
int main(){
	#ifndef ONLINE_JUDGE
freopen("input.txt", "r", stdin);
freopen("output.out", "w", stdout);
    #endif

    int var;
    cin>>var;
    for(int i=1; i<=10; i++){
      cout<<var * i<<endl;
    }
 return 0;
}