#include <iostream>
#include <bits/stdc++.h>
#include <string>
#include <map>
using namespace std;

#define DEBUG

//If error, but doesn't seem like it: Try updating vector<long long> to vector<long long>

//New idea: make two lists (maps so easy access) and aggregate repeats on each pass.

void printMap(map<long long, long long> stoneMap) {
    for (auto x : stoneMap) {
        for (int i = 0; i < x.second; i++) {
            cout << x.first << " ";
        }
    }
    cout << endl;
}

long long getMapSize(map<long long, long long> stoneMap) {
    long long total = 0;
    for (auto x : stoneMap) {
        total += x.second;
    }
    return total;
}

int intFromString(string s) {
    istringstream stream(s);
    int val;
    stream >> val;
    return val;
}

void addValuesToMap(long long val, long long valMult, map<long long, long long>& stoneMap) {
    if (stoneMap.count(val) == 0) {
        stoneMap[val] = valMult;
        return;
    }
    stoneMap[val] += valMult;
}

void makeNextStone(long long currentStoneVal, long long currentStoneMult, map<long long, long long>& nextStoneMap) {
    string stoneListString = to_string(currentStoneVal);
    
    if (currentStoneVal == 0) {
        addValuesToMap(1, currentStoneMult, nextStoneMap);
    } else if (stoneListString.size() % 2 == 0) {
        string firstHalf;
        string secondHalf;
        for (int i = 0; i < stoneListString.size() / 2; i++) {
            firstHalf.push_back(stoneListString[i]);
        }
        for (int i = stoneListString.size() / 2; i < stoneListString.size(); i++) {
            secondHalf.push_back(stoneListString[i]);
        }
        addValuesToMap(intFromString(firstHalf), currentStoneMult, nextStoneMap);
        addValuesToMap(intFromString(secondHalf), currentStoneMult, nextStoneMap);
    } else {
        addValuesToMap(currentStoneVal *= 2024, currentStoneMult, nextStoneMap);
    }
}

int main() {
    ifstream inputFile("AOC11.txt");
    string line;

    int currentStone;
    map<long long, long long> stoneMap1;
    map<long long, long long> stoneMap2;
    bool onStoneMap1 = true;
    const int blinks = 75;

    getline(inputFile, line);
    istringstream lineStream(line);

    //Get values in map
    while (lineStream >> currentStone)
        addValuesToMap(currentStone, 1, stoneMap1);

    #ifdef DEBUG
    printMap(stoneMap1);
    #endif

    for (int i = 0; i < blinks; i++) {
        cout << i << endl;
        if (onStoneMap1) {
            for (auto currentStoneVal : stoneMap1) {
                makeNextStone(currentStoneVal.first, currentStoneVal.second, stoneMap2);
            }
            stoneMap1.clear();
            onStoneMap1 = false;
        } else {
            for (auto currentStoneVal : stoneMap2) {
                makeNextStone(currentStoneVal.first, currentStoneVal.second, stoneMap1);
            }
            stoneMap2.clear();
            onStoneMap1 = true;
        }
    }

    #ifdef DEBUG
    #endif

    if (onStoneMap1) {
        cout << getMapSize(stoneMap1);
    } else {
        cout << getMapSize(stoneMap2);
    }


}