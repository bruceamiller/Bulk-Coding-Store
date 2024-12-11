#include <iostream>
#include <bits/stdc++.h>
#include <string>
#include <map>
using namespace std;

#define DEBUG

//If error, but doesn't seem like it: Try updating vector<long long> to vector<long long>

//New idea: make two lists and aggregate repeats.

void printMap(map<long long, long long> stoneMap) {
    for (auto x : stoneMap) {
        for (int i = 0; i < x.second; i++) {
            cout << x.first << " ";
        }
    }
    cout << endl;
}

int intFromString(string s) {
    istringstream stream(s);
    int val;
    stream >> val;
    return val;
}

int addValuesToMap(long long val, long long valMult, map<long long, long long>& stoneMap) {
    if (stoneMap.count(val)) {
        
    }
}

void updateStone(int& currentStonePos, vector<long long>& stoneList) {
    string stoneListString = to_string(stoneList[currentStonePos]);
    
    if (stoneList[currentStonePos] == 0) {
        stoneList[currentStonePos] = 1;
    } else if (stoneListString.size() % 2 == 0) {
        string firstHalf;
        string secondHalf;
        for (int i = 0; i < stoneListString.size() / 2; i++) {
            firstHalf.push_back(stoneListString[i]);
        }
        for (int i = stoneListString.size() / 2; i < stoneListString.size(); i++) {
            secondHalf.push_back(stoneListString[i]);
        }
        stoneList[currentStonePos] = intFromString(secondHalf);
        stoneList.insert(stoneList.begin() + currentStonePos, intFromString(firstHalf));
        currentStonePos++;
    } else {
        stoneList[currentStonePos] *= 2024;
    }
}

int main() {
    ifstream inputFile("AOC11.txt");
    string line;

    int currentStone;
    map<long long, long long> stoneMap1;
    map<long long, long long> stoneMap2;
    bool onStoneMap1 = true;
    const int blinks = 25;

    getline(inputFile, line);
    istringstream lineStream(line);

    //Get values in map
    while (lineStream >> currentStone)
        stoneMap1[currentStone] = 1;

    #ifdef DEBUG
    printMap(stoneMap1);
    #endif

    for (int i = 0; i < blinks; i++) {
        if (onStoneMap1) {
            for (auto x : stoneMap) {
                for (int i = 0; i < x.second; i++) {
                    cout << x.first << " ";
                }
            }
        }
    }

    #ifdef DEBUG
    #endif


}