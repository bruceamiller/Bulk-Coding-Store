#include <iostream>
#include <bits/stdc++.h>
#include <string>

using namespace std;

int currentPosInFinalTrails(array<int, 2> currentPos, vector<array<int, 2>>& visitedFinalTrails) {
    for (int i = 0; i < visitedFinalTrails.size(); i++) {
        if (currentPos == visitedFinalTrails[i]) {
            return true;
        }
    }
    return false;
}

int getAmountOfHigherTrails(array<int, 2> currentPos, vector<string>& topographyMap, int currentDepth, vector<array<int, 2>>& visitedFinalTrails) {
    vector<char> topographyNums = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'};
    if (currentDepth == 9 and !currentPosInFinalTrails(currentPos, visitedFinalTrails)) {
        visitedFinalTrails.push_back(currentPos);
        return 1;
    }
    
    int currentTotal = 0;

    //Up
    if (-1 < currentPos[0] - 1 and topographyMap[currentPos[0] - 1][currentPos[1]] == topographyNums[currentDepth + 1]) {
        currentTotal += getAmountOfHigherTrails({currentPos[0] - 1, currentPos[1]}, topographyMap, currentDepth + 1, visitedFinalTrails);
    }
    //Down
    if (currentPos[0] + 1 < topographyMap.size() and topographyMap[currentPos[0] + 1][currentPos[1]] == topographyNums[currentDepth + 1]) {
        currentTotal += getAmountOfHigherTrails({currentPos[0] + 1, currentPos[1]}, topographyMap, currentDepth + 1, visitedFinalTrails);
    }
    //Left
    if (-1 < currentPos[1] - 1 and topographyMap[currentPos[0]][currentPos[1] - 1] == topographyNums[currentDepth + 1]) {
        currentTotal += getAmountOfHigherTrails({currentPos[0], currentPos[1] - 1}, topographyMap, currentDepth + 1, visitedFinalTrails);
    }
    //Right
    if (currentPos[1] + 1 < topographyMap[0].size() and topographyMap[currentPos[0]][currentPos[1] + 1] == topographyNums[currentDepth + 1]) {
        currentTotal += getAmountOfHigherTrails({currentPos[0], currentPos[1] + 1}, topographyMap, currentDepth + 1, visitedFinalTrails);
    }
    return currentTotal;
}

int getAllTrails(array<int, 2>currentPos, vector<string>& topographicMap) {
    vector<array<int, 2>> visitedFinalTrails;
    return getAmountOfHigherTrails( currentPos, topographicMap, 0, visitedFinalTrails);
}



//Start at each trail head.
//Navigate through every possible position of the map, increasing in number as you go and add it all together.
//Recursive?

int main() {
    ifstream inputFile("AOC10.txt");
    string line;
    vector<string> topographyMap;


    while(getline(inputFile, line))
        topographyMap.push_back(line);

    int total = 0;

    for (int i = 0; i < topographyMap.size(); i++) {
        for (int j = 0; j < topographyMap[i].size(); j++) {
            if (topographyMap[i][j] == '0') {
                total += getAllTrails({i, j}, topographyMap);
            }
        }
    }

    cout << total;

}