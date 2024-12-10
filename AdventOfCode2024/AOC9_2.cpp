#include <iostream>
#include <bits/stdc++.h>
#include <string>

using namespace std;

//#define DEBUG

int intFromChar(char c) {
    istringstream stream({c});
    int val;
    stream >> val;
    return val;
}

void incrementStringPos(int& currentPos, string s) {
    currentPos++;
    if (currentPos == s.size())
        currentPos = 0;
}

int findFirstBlankPosOfSize(int& size, vector<int> dataLine) {
    int pos;
    int currentBlankSize = 0;
    for (pos = 0; pos < dataLine.size(); pos++) {
        if (dataLine[pos] == -1) {
            currentBlankSize++;
        } else {
            currentBlankSize = 0;
        }
        if (currentBlankSize == size) {
            return pos - currentBlankSize + 1;
        }
    }
    return pos;
}

pair<int, int> getLastFileBlockPosAndSize(vector<int> dataLine, int pos) {
    while(dataLine[pos] == -1) {
        pos--;
    }
    int currentBlockVal = dataLine[pos];
    int blockSize = 0;
    while(dataLine[pos] == currentBlockVal) {
        blockSize++;
        pos--;
    }
    pos++;
    return pair(pos, blockSize);
}

void swapBlockAndBlank(int blankPos, int blockPos, int blockSize, vector<int>& dataLine) {
    for (int i = 0; i < blockSize; i++) {
        swap(dataLine[blankPos + i], dataLine[blockPos + i]);
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



    pair<int, int> rightBlockPosAndSize = pair(dataLine.size() - 1, 0);
    rightBlockPosAndSize = getLastFileBlockPosAndSize(dataLine, rightBlockPosAndSize.first);





    while (rightBlockPosAndSize.first != 0) {
        int leftPos = findFirstBlankPosOfSize(rightBlockPosAndSize.second, dataLine);

        //Check for each right block if there is a spot that it would fit to the left of its position. If so move it.
        if (leftPos < rightBlockPosAndSize.first) {
            swapBlockAndBlank(leftPos, rightBlockPosAndSize.first, rightBlockPosAndSize.second, dataLine);
        }
        rightBlockPosAndSize.first -=  1;
        rightBlockPosAndSize = getLastFileBlockPosAndSize(dataLine, rightBlockPosAndSize.first);
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

    //checkSum
    long long total = 0;
    for (int i = 0; i < dataLine.size(); i++) {
        if (dataLine[i] != -1) {
            total += i * dataLine[i];
        }
    }

    cout << total;

    return 0;
}
