#include <iostream>
#include <bits/stdc++.h>
#include <string>

using namespace std;

#define DEBUG

int intFromChar(char c) {
    istringstream stream({c});
    int val;
    stream >> val;
    return val;
}


void incrementRightToNextBlank(vector<int> s, int& currentPos) {
    while (s[currentPos] != -1) {
        currentPos++;
    }
}

void incrementLeftToNextNonBlank(vector<int> s, int& currentPos) {
    while (currentPos != -1 and s[currentPos] == -1) {
        currentPos--;
    }
}


int main() {
    ifstream inputFile("AOC9.txt");
    string inputLine;
    vector<int> dataLine;
    
    getline(inputFile, inputLine);

    bool onBlock = true;
    int currentBlockID = 0;

    string blockIDs = "0123456789";

    for (int i = 0; i < inputLine.size(); i++) {
        int currentLength = intFromChar(inputLine[i]);
        if (onBlock) {
            for (int j = 0; j < currentLength; j++) {
                dataLine.push_back(currentBlockID);
            }
            currentBlockID++;
        } else {
            for (int j = 0; j < currentLength; j++) {
                dataLine.push_back(-1);
            }
        }
        onBlock = !onBlock;
    }

    #ifdef DEBUG
    for(int i = 0; i < dataLine.size(); i++) {
        if (dataLine[i] == -1) {
            cout << '.';
        } else {
            cout << dataLine[i];
        }
    }
    cout << "\n\n";
    #endif

    int leftPos = 0;
    incrementRightToNextBlank(dataLine, leftPos);
    int rightPos = dataLine.size() - 1;
    incrementLeftToNextNonBlank(dataLine, rightPos);

    while (rightPos > leftPos) {
        swap(dataLine[leftPos], dataLine[rightPos]);
        incrementRightToNextBlank(dataLine, leftPos);
        incrementLeftToNextNonBlank(dataLine, rightPos);
    }

    #ifdef DEBUG
    for(int i = 0; i < dataLine.size(); i++) {
        if (dataLine[i] == -1) {
            cout << '.';
        } else {
            cout << dataLine[i];
        }
    }
    cout << "\n\n";
    #endif


    int checkPos = 0;
    long long total = 0;
    while (dataLine[checkPos] != -1) {
        total += checkPos * dataLine[checkPos];
        checkPos++;
    }

    cout << total;

    return 0;
}
