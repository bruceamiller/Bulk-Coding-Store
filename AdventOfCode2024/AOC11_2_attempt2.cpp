#include <iostream>
#include <bits/stdc++.h>
#include <string>
using namespace std;

#define DEBUG

//If error, but doesn't seem like it: Try updating vector<long long> to vector<long long>

void printList(vector<long long> list) {
    for (int i = 0; i < list.size(); i++) {

        cout << list[i] << " ";
    }
    cout << endl;
}

long long numFromString(string s) {
    istringstream stream(s);
    long long val;
    stream >> val;
    return val;
}

long long stonesAfterUpdates(long long currentStoneVal, int currentDepth, int maxDepth) {
    string currentStoneString = to_string(currentStoneVal);

    if (currentDepth == maxDepth) {
        return 1;
    } else if (currentStoneVal == 0) {
        return stonesAfterUpdates(1, currentDepth + 1, maxDepth);
    } else if (currentStoneString.size() % 2 == 0) {
        string firstHalf;
        string secondHalf;
        for (int i = 0; i < currentStoneString.size() / 2; i++) {
            firstHalf.push_back(currentStoneString[i]);
        }
        for (int i = currentStoneString.size() / 2; i < currentStoneString.size(); i++) {
            secondHalf.push_back(currentStoneString[i]);
        }
        return stonesAfterUpdates(numFromString(firstHalf), currentDepth + 1, maxDepth) + stonesAfterUpdates(numFromString(secondHalf), currentDepth + 1, maxDepth);
    } else {
        return stonesAfterUpdates(currentStoneVal * 2024, currentDepth + 1, maxDepth);
    }
}

int main() {
    ifstream inputFile("AOC11.txt");
    string line;

    int currentStoneVal;
    vector<long long> stoneList;
    const int blinks = 75;

    getline(inputFile, line);
    istringstream lineStream(line);

    while (lineStream >> currentStoneVal)
        stoneList.push_back(currentStoneVal);

    #ifdef DEBUG
    printList(stoneList);
    #endif

    long long stoneListSize = 0;

    for (int j = 0; j < stoneList.size(); j++) {
        cout << stoneListSize << " ";
        stoneListSize += stonesAfterUpdates(stoneList[j], 0, blinks);
    }
    cout << endl;


    cout << stoneListSize;

}

//Still too slow