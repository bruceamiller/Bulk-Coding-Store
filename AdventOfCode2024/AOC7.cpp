#include <iostream>
#include <bits/stdc++.h>
#include <string>
#include <vector>
using namespace std;


bool isRecursivePair(long long equationResult, vector<int> equationVals, int equationPos, long long currentResult);
//Recursive function that goes into the list
bool isSuitableEquation(long long equationResult, vector<int> equationVals) {
    return isRecursivePair(equationResult, equationVals, 1, equationVals[0]);
}

bool isRecursivePair(long long equationResult, vector<int> equationVals, int equationPos, long long currentResult) {
    if (equationPos == equationVals.size()) {
        if (currentResult == equationResult) {
            return true;
        }
        return false;
    }
    bool nextIsMultIsValid = isRecursivePair(equationResult, equationVals, equationPos + 1, currentResult * equationVals[equationPos]);
    bool nextIsAddIsValid = isRecursivePair(equationResult, equationVals, equationPos + 1, currentResult + equationVals[equationPos]);

    istringstream numStream(to_string(currentResult) + to_string(equationVals[equationPos]));
    long long concatenatedValue;
    numStream >> concatenatedValue;
    bool nextConcatenateIsValid = isRecursivePair(equationResult, equationVals, equationPos + 1, concatenatedValue);


    if (nextIsMultIsValid or nextIsAddIsValid or nextConcatenateIsValid) {
        return true;
    }
    return false;
}

int main() {
    ifstream inputFile("AOC7.txt");
    string line;
    vector<pair<long long, vector<int>>> equations;

    while (getline(inputFile, line)) {
        istringstream lineStream(line);
        long long newResult;
        int newElement;
        char dumpChar;
        vector<int> newEquationElements;

        lineStream >> newResult;
        lineStream >> dumpChar;
        while (lineStream >> newElement) {
            newEquationElements.push_back(newElement);
        }
        equations.push_back(pair(newResult, newEquationElements));
    }

    long long total = 0;

    for (int i = 0; i < equations.size(); i++) {
        if (isSuitableEquation(equations[i].first, equations[i].second)) {
            total += equations[i].first;            
        }
    }

    cout << total;
    return 0;
}