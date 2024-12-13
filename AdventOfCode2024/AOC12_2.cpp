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
    vector<array<int, 2>> adjacentTransformations = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
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

//Doesn't work for internal edges...
int countEdges(vector<array<int, 2>> connectedPlants, array<int, 2> startPos) {
    vector<array<int, 2>> moveDirections = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
    //Start with trying to go up, because first position should be highest first and then leftmost in the highest because of where it will be found in the grid.
    //Follow edge, which means going in the rotated 90 degree direction, until you can go the last direction, until you can't go either, then the last direction is rotated 90 degress.
    // Every change in direction makes a new edge;

    set<array<int, 2>> connectedPlantsSet;
    for (auto plantPos : connectedPlants) {
        connectedPlantsSet.insert(plantPos);
    }

    int edges = 0;
    int lastDirection = 0; //up
    array<int, 2> currentPos = startPos;
    while(currentPos != startPos or lastDirection != 0 or edges == 0) {
        //If not possible to move in lastDirection, then move rotated 90 degrees. If that's not possible, then rotate lastDirection.
        if (connectedPlantsSet.count({currentPos[0] + moveDirections[lastDirection][0], currentPos[1] + moveDirections[lastDirection][1]})) {
            currentPos[0] += moveDirections[lastDirection][0];
            currentPos[1] += moveDirections[lastDirection][1];
            edges += 2;
        } else if (connectedPlantsSet.count({currentPos[0] + moveDirections[rotatedDirectionPos(lastDirection, moveDirections, 1)][0], currentPos[1] + moveDirections[rotatedDirectionPos(lastDirection, moveDirections, 1)][1]})) {
            currentPos[0] += moveDirections[rotatedDirectionPos(lastDirection, moveDirections, 1)][0];
            currentPos[1] += moveDirections[rotatedDirectionPos(lastDirection, moveDirections, 1)][1];
        } else {
            lastDirection = rotatedDirectionPos(lastDirection, moveDirections, 1);
            edges++;
        }
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
                int edges = countEdges(connectedPlants, {i, j});
                total += connectedPlants.size() * edges;
            }
        }
    }

    cout << total;


    //Go through every position in the map.
    // If the position has not been taken by a region already, then

}