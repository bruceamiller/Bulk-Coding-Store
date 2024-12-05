#include <iostream>
#include <bits/stdc++.h>
#include <string>
#include <vector>
using namespace std;

//#define DEBUG

int horizontalMatches(string AStr, int AStrPos, string BStr);
int positiveDiagonalMatches(vector<string> AGrid, int AGridY, int AGridX, string BStr);
int negativeDiagonalMatches(vector<string> AGrid, int AGridY, int AGridX, string BStr);
int verticalMatches(vector<string> AGrid, int AGridY, int AGridX, string BStr);

int main() {
    ifstream inputFile("AOC4.txt");
    vector<string> inputGrid;
    string inputString;
    vector<string> xMasCombos =
    {"MAS", "SAM",
    "MAS", "MAS",
    "SAM", "MAS",
    "SAM", "SAM"};

    int total = 0;

    while (getline(inputFile, inputString)) {
        inputGrid.push_back(inputString);
    }

    for (int line = 0; line < inputGrid.size() - 2; line++) {
        for (int i = 0; i < inputGrid[line].size() - 2; i++) {
            for (int j = 0; j < xMasCombos.size(); j += 2) {
                if (negativeDiagonalMatches(inputGrid, line, i, xMasCombos[j]) and positiveDiagonalMatches(inputGrid, line, i+2, xMasCombos[j+1])) {
                    total++;
                }
            }

        }
    }


    cout << total;
    return 0;
}

int horizontalMatches(string AStr, int AStrPos, string BStr) {
    for (int j = 0; j < BStr.size(); j++) {
        if (AStr[AStrPos + j] != BStr[j]) {
            return false;
        }
    }
    return true;
}

int negativeDiagonalMatches(vector<string> AGrid, int AGridY, int AGridX, string BStr) {
    for (int j = 0; j < BStr.size(); j++) {
        if (AGrid[AGridY+j][AGridX+j] != BStr[j]) {
            return false;
        }
    }
    return true;
}


int positiveDiagonalMatches(vector<string> AGrid, int AGridY, int AGridX, string BStr) {
    for (int j = 0; j < BStr.size(); j++) {
        if (AGrid[AGridY+j][AGridX-j] != BStr[j]) {
            return false;
        }
    }
    return true;
}

int verticalMatches(vector<string> AGrid, int AGridY, int AGridX, string BStr) {
    for (int j = 0; j < BStr.size(); j++) {
        if (AGrid[AGridY+j][AGridX] != BStr[j]) {
            return false;
        }
    }
    return true;
}

//Small scale matches: 
// Horizontal matches: 3, 2
// Positive Diagonal Matches: 1, 4
// Negative Diagonal Matches: 1, 4
// Vertical Matches: 1, 2