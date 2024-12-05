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

    int total;

    while (getline(inputFile, inputString)) {
        inputGrid.push_back(inputString);
    }

    #ifdef DEBUG
        cout << "Horizontal Matches: ";  
    #endif
    for (int line = 0; line < inputGrid.size(); line++) {
        for (int i = 0; i < inputGrid[line].size() - 3; i++) {
            if (horizontalMatches(inputGrid[line], i, "XMAS")) {
                total++;
                #ifdef DEBUG
                cout << "X";
                #endif
            }   
            if (horizontalMatches(inputGrid[line], i, "SAMX")) {
                total++;
                #ifdef DEBUG
                cout << "Y";
                #endif
            }
        }
    }

    #ifdef DEBUG
        cout << endl << "Negative Diagonal And Vertical Matches: ";
    #endif
    for (int line = 0; line < inputGrid.size() - 3; line++) {
        for (int i = 0; i < inputGrid[line].size(); i++) {
            //Diagonal checks on each line
            if (negativeDiagonalMatches(inputGrid, line, i, "XMAS")){
                total++;
                #ifdef DEBUG
                cout << "X";
                #endif
            }   
            if (negativeDiagonalMatches(inputGrid, line, i, "SAMX")){
                total++;
                #ifdef DEBUG
                cout << "Y";
                #endif
            }   
            //Vertical checks on each line
            if (verticalMatches(inputGrid, line, i, "XMAS")){
                total++;
                #ifdef DEBUG
                cout << "Z";
                #endif
            }   
            if (verticalMatches(inputGrid, line, i, "SAMX")){
                total++;
                #ifdef DEBUG
                cout << "A";
                #endif
            }   
        }
    }

    #ifdef DEBUG
        cout << endl << "Positive Diagonal Matches: ";
    #endif
    for (int line = 0; line < inputGrid.size() - 3; line++) {
        for (int i = 3; i < inputGrid[line].size(); i++) {
            //Diagonal checks on each line
            if (positiveDiagonalMatches(inputGrid, line, i, "XMAS")) {
                total++;
                #ifdef DEBUG
                cout << "X";
                #endif
            }   

            if (positiveDiagonalMatches(inputGrid, line, i, "SAMX")){
                total++;
                #ifdef DEBUG
                cout << "X";
                #endif
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