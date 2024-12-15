#include <iostream>
#include <bits/stdc++.h>
#include <string>
#include <set>
using namespace std;

#define DEBUG

vector<array<int, 2>> getAdjacentPlants(array<int, 2> currentPlantPos, vector<string> plantGrid) {
    vector<array<int, 2>> adjacentTransformations = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    vector<array<int, 2>> outputPlants;

    for (int i = 0; i < adjacentTransformations.size(); i++) {
        array<int, 2> transformedPos = {currentPlantPos[0] + adjacentTransformations[i][0], currentPlantPos[1] + adjacentTransformations[i][1]};
        if (-1 < transformedPos[0] and transformedPos[0] < plantGrid.size() and -1 < transformedPos[1] and transformedPos[1] < plantGrid[0].size()) {
            if (plantGrid[currentPlantPos[0]][currentPlantPos[1]] == plantGrid[transformedPos[0]][transformedPos[1]]) {
                outputPlants.push_back(transformedPos);
            }
        }
    }

    return outputPlants;
}

vector<array<int, 2>> getAdjacentPlantsDifferingValue(array<int, 2> currentPlantPos, vector<string> plantGrid) {
    vector<array<int, 2>> adjacentTransformations = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    vector<array<int, 2>> outputPlants;

    for (int i = 0; i < adjacentTransformations.size(); i++) {
        array<int, 2> transformedPos = {currentPlantPos[0] + adjacentTransformations[i][0], currentPlantPos[1] + adjacentTransformations[i][1]};
        if (-1 < transformedPos[0] and transformedPos[0] < plantGrid.size() and -1 < transformedPos[1] and transformedPos[1] < plantGrid[0].size()) {
            if (plantGrid[currentPlantPos[0]][currentPlantPos[1]] != plantGrid[transformedPos[0]][transformedPos[1]]) {
                outputPlants.push_back(transformedPos);
            }
        }
    }

    return outputPlants;
}

vector<array<int, 2>> getConnectedPlants(array<int, 2> currentPlantPos, vector<string> plantGrid) {
    set<array<int, 2>> connectPlantsSet = {currentPlantPos};

    bool newChanges = true;
    while (newChanges == true) {
        newChanges = false;
        for (auto setVal : connectPlantsSet) {
            vector<array<int, 2>> newSetVals = getAdjacentPlants(setVal, plantGrid);
            for (int i = 0; i < newSetVals.size(); i++) {
                if (connectPlantsSet.count(newSetVals[i]) == 0) {
                    connectPlantsSet.insert(newSetVals[i]);
                    newChanges = true;
                }
            }
        }
    }

    vector<array<int, 2>> connectPlantsList;

    for (auto setVal : connectPlantsSet) {
        connectPlantsList.push_back(setVal);
    }

    return connectPlantsList;
}

void fillConnectedEdgesWTrue(vector<array<int, 2>> connectedPlants, vector<vector<bool>>& alreadyMappedPositions) {
    for (auto plantPos : connectedPlants) {
        alreadyMappedPositions[plantPos[0]][plantPos[1]] = 1;
    }
}

int perimeter(vector<array<int, 2>> connectedPlants) {
    vector<array<int, 2>> adjacentTransformations = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}, {1, 1}, {1, -1}, {-1, 1}, {-1, -1}};
    set<array<int, 2>> alreadyCalculatedPlantsWFence;

    int perimeter = 0;
    for (auto currentPlantPos: connectedPlants) {
        perimeter += 4;
        for (int i = 0; i < adjacentTransformations.size(); i++) {
            array<int, 2>transformedPlantPos = {currentPlantPos[0] + adjacentTransformations[i][0], currentPlantPos[1] + adjacentTransformations[i][1]};
            if (alreadyCalculatedPlantsWFence.count(transformedPlantPos) == 1) {
                perimeter -= 2;
            }
        }
        alreadyCalculatedPlantsWFence.insert(currentPlantPos);
    }
    return perimeter;
}

int rotatedDirectionPos(int currentDirectionPos, vector<array<int, 2>> directions, int rotations) {
    return (currentDirectionPos + rotations) % directions.size();
}

array<int, 2> addTwoPositions (array<int, 2> pos1, array<int, 2> pos2) {
    return {pos1[0] + pos2[0], pos1[1] + pos2[1]};
}


bool plantInPlantAndEdgesSetAndHasMatchingLine(array<int, 2> plantPos, set<pair<array<int, 2>, array<bool, 4>>> plantAndEdgesSet, int lineDirection) {
    for (pair<array<int, 2>, array<bool, 4>> plantAndEdges : plantAndEdgesSet) {
        if ((plantAndEdges.first == plantPos) and plantAndEdges.second[lineDirection] == 1) {
            return true;
        }
    }
    return false;
}

int countEdges(vector<array<int, 2>> connectedPlants, vector<string> plantGrid) {
    vector<array<int, 2>> directionalTransformations = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}}; //up, right, down, left

    set<array<int, 2>> connectedPlantsSet;
    for (array<int, 2> currentPlantPos: connectedPlants) { // Add each square
        connectedPlantsSet.insert(currentPlantPos);
    }
    
    //Go through every plant, and start counting edges
    //If edge is in line with edge that already exists and next to it, then no new edges are added.
    //If edge bridges gap between two edges in line, edges is reduced by one.
    //Otherwise if an unconnected edge is made, you get 1 new edge.

    int edges = 0;

    set<pair<array<int, 2>, array<bool, 4>>> alreadyCountedEdges; //each set: pair({squareX, squareY}, {edgeUp, edgeRight, edgeDown, edgeLeft})
    for (array<int, 2> currentPlantPos: connectedPlants) { // Add each square
        pair<array<int, 2>, array<bool, 4>> currentPlantPosAndEdges;
        currentPlantPosAndEdges.first = currentPlantPos;
        currentPlantPosAndEdges.second = {0, 0, 0, 0};
        for (int direction = 0; direction < directionalTransformations.size(); direction++) {
            if (connectedPlantsSet.count(addTwoPositions(currentPlantPos, directionalTransformations[direction])) == 0) {
                int adjacentEdgesInLine = 0;
                array<int, 2> adjacentPos1 = addTwoPositions(currentPlantPos, directionalTransformations[rotatedDirectionPos(direction, directionalTransformations, -1)]);
                adjacentEdgesInLine += plantInPlantAndEdgesSetAndHasMatchingLine(adjacentPos1, alreadyCountedEdges, direction);
                array<int, 2> adjacentPos2 = addTwoPositions(currentPlantPos, directionalTransformations[rotatedDirectionPos(direction, directionalTransformations, 1)]);
                adjacentEdgesInLine += plantInPlantAndEdgesSetAndHasMatchingLine(adjacentPos2, alreadyCountedEdges, direction);
                if (adjacentEdgesInLine == 0) { // Zero edges connected and in line, so a new edge is made. +1 total edges.
                    edges++;
                } else if (adjacentEdgesInLine == 2) { // Two edges connected and in line, so they are merged into one edge. -1 total edges.
                    edges--;
                } // Else, if in line with only one edge connected and in line, meaning that edge is just extended.
            
                currentPlantPosAndEdges.second[direction] = 1;
            }
        }
        alreadyCountedEdges.insert(currentPlantPosAndEdges);
    }
    return edges;
}

int main() {
    ifstream inputFile("AOC12.txt");
    string line;
    vector<string> plantGrid;
    vector<vector<bool>> alreadyMappedPositions;



    //Get grid and empty grid
    while (getline(inputFile, line)) {
        vector<bool> alreadyMappedLine;
        plantGrid.push_back(line);
        for (int i = 0; i < line.size(); i++) {
            alreadyMappedLine.push_back(0);
        }
        alreadyMappedPositions.push_back(alreadyMappedLine);
    }

    #ifdef DEBUG
    for (int i = 0; i < plantGrid.size(); i++) {
        cout << plantGrid[i] << endl;
    }
    #endif


    int total = 0;

    for (int i = 0; i < plantGrid.size(); i++) {
        for (int j = 0; j < plantGrid[0].size(); j++) {
            if (alreadyMappedPositions[i][j] == 0) {
                vector<array<int, 2>> connectedPlants = getConnectedPlants({i, j}, plantGrid);
                fillConnectedEdgesWTrue(connectedPlants, alreadyMappedPositions);
                int edges = countEdges(connectedPlants, plantGrid);
                total += connectedPlants.size() * edges;
            }
        }
    }

    cout << total;


    //Go through every position in the map.
    // If the position has not been taken by a region already, then

}