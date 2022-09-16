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

#define sp << " "
#define lin << "\n"

int main() {
    vector<int> ratings{1, 2, 3, 4, 5, 5, 1};
    vector<int> candies;
    for (int i = 0; i < ratings.size(); i++){
        candies.push_back(1);
    }

    vector<int> mins;
    if (ratings[0] <= ratings[1]){
        mins.push_back(0);
    }
    for (int i = 1; i < ratings.size()-1; i++){
        if (ratings[i] <= ratings[i+1] && ratings[i-1] >= ratings[i]){
            mins.push_back(i);
        }
    }
    if (ratings[ratings.size()-1] <= ratings[ratings.size()-2]){
        mins.push_back(ratings.size()-1);
    }


    int child;
    for(int x:mins){
        child = x;
        while (child-1 >= 0 && ratings[child-1] > ratings[child]){
            /*if(ratings[child-1] == ratings[child]){
                candies[child-1] = candies[child];
            }else{*/
            candies[child-1] = max(candies[child-1], candies[child]+1);
            //}
            child--;
        }

        child = x;
        while (child+1 < ratings.size() && ratings[child+1] > ratings[child]){
            /*if(ratings[child+1] == ratings[child]){
                candies[child+1] = candies[child];
            }else{*/
            candies[child+1] = max(candies[child+1], candies[child]+1);
            //}
            child++;
        }
    }

    for (int x:candies){
        cout << x sp;
    }

    return 0;
}