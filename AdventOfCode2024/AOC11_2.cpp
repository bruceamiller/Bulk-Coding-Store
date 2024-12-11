#include <iostream>
#include <bits/stdc++.h>
#include <string>
using namespace std;

//#define DEBUG

//If error, but doesn't seem like it: Try updating list<long long> to list<long long>

void printList(list<long long> list) {
    for (int num : list) {
        cout << num << " ";
    }
    cout << endl;
}

int intFromString(string s) {
    istringstream stream(s);
    int val;
    stream >> val;
    return val;
}

void updateStone(list<long long>::iterator currentStonePos, list<long long>& stoneList) {
    string stoneListString = to_string(*currentStonePos);
    
    if (*currentStonePos == 0) {
        *currentStonePos = 1;
    } else if (stoneListString.size() % 2 == 0) {
        string firstHalf;
        string secondHalf;
        for (int i = 0; i < stoneListString.size() / 2; i++) {
            firstHalf.push_back(stoneListString[i]);
        }
        for (int i = stoneListString.size() / 2; i < stoneListString.size(); i++) {
            secondHalf.push_back(stoneListString[i]);
        }
        *currentStonePos = intFromString(secondHalf);
        stoneList.insert(currentStonePos, intFromString(firstHalf));
        currentStonePos++;
    } else {
        *currentStonePos *= 2024;
    }
}

int main() {
    ifstream inputFile("AOC11.txt");
    string line;

    int currentStone;
    list<long long> stoneList;
    const int blinks = 75;

    getline(inputFile, line);
    istringstream lineStream(line);

    while (lineStream >> currentStone)
        stoneList.push_back(currentStone);

    #ifdef DEBUG
    printList(stoneList);
    #endif


    for (int i = 0; i < blinks; i++) {
        cout << i << " - " << stoneList.size() << endl;
        for (list<long long>::iterator it = stoneList.begin(); it != stoneList.end(); ++it) {
            updateStone(it, stoneList);
        }

    }

    #ifdef DEBUG
    printList(stoneList);
    #endif

    cout << blinks << " - " << stoneList.size() << endl;
}

#include <iostream>
#include <bits/stdc++.h>
#include <string>
using namespace std;

//#define DEBUG

//If error, but doesn't seem like it: Try updating list<long long> to list<long long>

void printList(list<long long> list) {
    for (int num : list) {
        cout << num << " ";
    }
    cout << endl;
}

int intFromString(string s) {
    istringstream stream(s);
    int val;
    stream >> val;
    return val;
}

void updateStone(list<long long>::iterator currentStonePos, list<long long>& stoneList) {
    string stoneListString = to_string(*currentStonePos);
    
    if (*currentStonePos == 0) {
        *currentStonePos = 1;
    } else if (stoneListString.size() % 2 == 0) {
        string firstHalf;
        string secondHalf;
        for (int i = 0; i < stoneListString.size() / 2; i++) {
            firstHalf.push_back(stoneListString[i]);
        }
        for (int i = stoneListString.size() / 2; i < stoneListString.size(); i++) {
            secondHalf.push_back(stoneListString[i]);
        }
        *currentStonePos = intFromString(secondHalf);
        stoneList.insert(currentStonePos, intFromString(firstHalf));
        currentStonePos++;
    } else {
        *currentStonePos *= 2024;
    }
}

int main() {
    ifstream inputFile("AOC11.txt");
    string line;

    int currentStone;
    list<long long> stoneList;
    const int blinks = 75;

    getline(inputFile, line);
    istringstream lineStream(line);

    while (lineStream >> currentStone)
        stoneList.push_back(currentStone);

    #ifdef DEBUG
    printList(stoneList);
    #endif


    for (int i = 0; i < blinks; i++) {
        cout << i << " - " << stoneList.size() << endl;
        for (list<long long>::iterator it = stoneList.begin(); it != stoneList.end(); ++it) {
            updateStone(it, stoneList);
        }

    }

    #ifdef DEBUG
    printList(stoneList);
    #endif

    cout << blinks << " - " << stoneList.size() << endl;
}