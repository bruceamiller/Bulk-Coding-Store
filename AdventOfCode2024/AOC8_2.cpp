#include <iostream>
#include <bits/stdc++.h>
#include <string>
#include <vector>
using namespace std;

int getPosInUniquePoints(char antennaValue, vector<pair<char, vector<array<int, 2>>>> uniquePoints) {
    for (int i = 0; i < uniquePoints.size(); i++) {
        if (uniquePoints[i].first == antennaValue) {
            return i;
        }
    }
    return -1;
}

void insertAntinodeIntoUniquePoints(char antennaValue, array<int, 2> antennaPos, vector<pair<char, vector<array<int, 2>>>>& uniquePoints) {
    int uniquePointPos = getPosInUniquePoints(antennaValue, uniquePoints);
    if (uniquePointPos == -1) { //if point not in array
        vector<array<int, 2>> newAntennaPosArray = {antennaPos};
        uniquePoints.push_back(pair(antennaValue,newAntennaPosArray));
        return;
    }
    uniquePoints[uniquePointPos].second.push_back(antennaPos);
}

array<int, 2> getAntinode(array<int, 2> point1, array<int, 2> point2) {
    array<int, 2> outputPoint;
    outputPoint[0] = point1[0] + (point2[0] - point1[0]) * 2;
    outputPoint[1] = point1[1] + (point2[1] - point1[1]) * 2;
    return outputPoint;
}

bool pointWithinGrid(vector<string> antinodeGrid, array<int, 2> point) {
    if (-1 < point[0] and point[0] < antinodeGrid.size() and -1 < point[1] and point[1] < antinodeGrid[0].size()) {
        return true;
    }
    return false;
}

void placeAntinodePoints(vector<string> antennaGrid, vector<string>& antinodeGrid, pair<char, vector<array<int, 2>>> uniquePoints){
    for (int i = 0; i < uniquePoints.second.size(); i++) {
        for (int j = 0; j < uniquePoints.second.size(); j++) {
            array<int, 2> antinodePosTemp = uniquePoints.second[j];
            array<int, 2> antinodePos = getAntinode(uniquePoints.second[i], uniquePoints.second[j]);

            while (pointWithinGrid(antinodeGrid, antinodePos) and i != j) {
                antinodeGrid[antinodePos[0]][antinodePos[1]] = '#';
                array<int, 2> newAntinodePos = getAntinode(antinodePosTemp, antinodePos);
                antinodePosTemp = antinodePos;
                antinodePos = newAntinodePos;
            }
        }
    }
}



int main() {
    ifstream inputFile("AOC8.txt");
    string line;
    vector<string> antennaGrid;
    vector<string> antinodeGrid;
    
    //Get grid with antennas, and empty grid to put antinodes
    while (getline(inputFile, line)) {
        antennaGrid.push_back(line);
        string emptyLine = line;
        for (int i = 0; i < emptyLine.size(); i++) {
            emptyLine[i] = '.';
        }
        antinodeGrid.push_back(emptyLine);
    }

    vector<pair<char, vector<array<int, 2>>>> uniquePoints; //Array of pairs of each antenna type and all of its locations


    for (int i = 0; i < antennaGrid.size(); i++) {
        for (int j = 0; j < antennaGrid[0].size(); j++) {
            if (antennaGrid[i][j] != '.') {
                array<int, 2> currentPos;
                currentPos[0] = i;
                currentPos[1] = j;
                insertAntinodeIntoUniquePoints(antennaGrid[i][j], currentPos, uniquePoints);
                antinodeGrid[i][j] = '#';
            }
        }
    }

    for (int i = 0; i < uniquePoints.size(); i++) {
        placeAntinodePoints(antennaGrid, antinodeGrid, uniquePoints[i]);
    }

    for (int i = 0; i < antinodeGrid.size(); i++) {
        cout << antinodeGrid[i] << endl;
    }

    int total = 0;

    for (int i = 0; i < antinodeGrid.size(); i++) {
        for (int j = 0; j < antinodeGrid[0].size(); j++) {
            if (antinodeGrid[i][j] == '#') {
                total++;
            }
        }
    }

    cout << total;
}