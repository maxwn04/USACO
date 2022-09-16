#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    ofstream fout ("test.out", ios::out);
    ifstream fin ("test.in", ios::in);
    int n;
    fin >> n;
    int timeIn, timeSpent;
    map<int, vector<int>> startToPrio;
    vector<int> prioToStart;
    vector<int> prioToDuration;

    for (int i = 0; i < n; i++) {
    	fin >> timeIn >> timeSpent;
        if (startToPrio.count(timeIn) == 0) {
            startToPrio.insert(pair<int, vector<int>>(timeIn, {}));
        }
    	startToPrio[timeIn].push_back(i);
    	prioToStart.push_back(timeIn);
    	prioToDuration.push_back(timeSpent);
    }
    vector<int> arrivalOrder;
    for (map<int, vector<int>>::iterator itr = startToPrio.begin(); itr != startToPrio.end(); ++itr) {
        //cerr << itr->first << " " << itr->second << "\n";
        //fout << itr->first << " ";
        for (int i = 0; i < itr->second.size(); i++){
            arrivalOrder.push_back(itr->second[i]);
        }
        
    }
    // for (int i = 0; i < n; i++) {
    //     cerr << " " << arrivalOrder[i];
    // }
    int time = prioToStart[arrivalOrder[0]];
    int endTime = time + prioToDuration[arrivalOrder[0]];
    int enterTime, priority, curTasting;
    vector<int> order = {arrivalOrder[0]};
    vector<int> queue;
    int maxTime = 0;
    int wait;
    for (int i = 0; i < n-1; i++) {
        enterTime = prioToStart[arrivalOrder[i+1]];
        priority = arrivalOrder[i+1];
        while (enterTime > endTime && queue.size() > 0) {
            curTasting = queue[0];
            wait = endTime - prioToStart[queue[0]];
            if (wait > maxTime) {
                maxTime = wait;
            }
            queue.erase(queue.begin());
            order.push_back(curTasting);
            time = endTime;
            endTime = time + prioToDuration[curTasting];
        }
        queue.push_back(priority);
        sort (begin(queue), end(queue));
        /*cerr << "\n" << i;
        for (int i = 0; i < queue.size(); i++) {
            cerr << " " << queue[i];
        }*/
    }


    for (int i = 0; i < queue.size(); i++) {
        order.push_back(queue[i]);
    }
    // cerr << "Final Order ";
    // for (int i = 0; i < n; i++) {
    //     cerr << order[i] << " \n" ;
    // }
    
    time = endTime;
    for (int i = 0; i < queue.size(); i++) {
        //cerr << "\n"<< i;
        if (prioToStart[queue[i]] > time) {
            time = prioToStart[queue[i]];
        }
        wait = time - prioToStart[queue[i]];
        // cerr << wait << " " << order[i] << '\n';
        if (wait > maxTime) {
            maxTime = wait;
        }
        time += prioToDuration[queue[i]];
    }
    fout << maxTime;

    return 0;
}

