#include <iostream>
#include <bits/stdc++.h>
#include <string>
using namespace std;

//#define DEBUG

//If error, but doesn't seem like it: Try updating vector<long long> to vector<long long>

void printList(vector<long long> list) {
    for (int i = 0; i < list.size(); i++) {

        cout << list[i] << " ";
    }
    cout << endl;
}

int intFromString(string s) {
    istringstream stream(s);
    int val;
    stream >> val;
    return val;
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
    vector<long long> stoneList;
    const int blinks = 25;

    getline(inputFile, line);
    istringstream lineStream(line);

    while (lineStream >> currentStone)
        stoneList.push_back(currentStone);

    #ifdef DEBUG
    printList(stoneList);
    #endif

    for (int i = 0; i < blinks; i++) {
        //cout << i << endl;
        for (int j = 0; j < stoneList.size(); j++) {
            updateStone(j, stoneList);
        }
    }

    #ifdef DEBUG
    printList(stoneList);
    #endif

    cout << stoneList.size();

}