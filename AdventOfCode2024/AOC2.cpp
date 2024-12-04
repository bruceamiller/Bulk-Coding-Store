#include <iostream>
#include <bits/stdc++.h>
#include <string>
#include <sstream>
using namespace std;

void MergeSort(vector<int>& array);
void MergeSortRecursion(vector<int>& array, int l, int r);
void MergeSortedArraysV1 (vector<int>& array, int l, int m, int r);

bool isValid(vector<int>& curLineVals);

bool isValidWCheck(vector<int>& curLineVals) {
    //If it's just valid it's valid.
    if (isValid(curLineVals)) {
        return true;
    } else { //If it's not valid, try removing every individual, to be valid.
        for (int i = 0; i < curLineVals.size(); i++) {
            vector<int> tempLineVals = curLineVals;
            tempLineVals.erase(tempLineVals.begin() + i);
            if (isValid(tempLineVals)) return true;
        }
    }

    
    return false;
}

bool isValid(vector<int>& curLineVals) {
    if (curLineVals[0] > curLineVals[1]) { //Decreasing
        for (int i = 0; i < curLineVals.size() - 1; i++) {
            if (!(0 < curLineVals[i] - curLineVals[i + 1] and curLineVals[i] - curLineVals[i + 1] < 4)) {
                return false;
            }
        }
    } else {
        for (int i = 0; i < curLineVals.size() - 1; i++) {
            if (!(0 < curLineVals[i + 1] - curLineVals[i] and curLineVals[i + 1] - curLineVals[i] < 4)) {
                return false;
            }
        }
    }
    return true;
}


int main() {
    ifstream inputFile("AOC2.txt");
    string inputString;

    int total = 0;
    int currentLine = 0;

    while (getline(inputFile, inputString)) {
        istringstream inputStream(inputString);
        
        //Collect values in an array.
        vector<int> curLineVals;
        int nextValue;
        while (inputStream >> nextValue ) {
            curLineVals.push_back(nextValue);
        }

        //Is valid on first pass
        /*
        if (isValid(curLineVals)) {
            total++;
        }
        */

        //Is valid even with one value removed, if not initially valid.
        if (isValidWCheck(curLineVals)) {
            total++;
        }
    }

    cout << total;
    return 0;
}