#include <iostream>
#include <bits/stdc++.h>
#include <string>
#include <vector>
using namespace std;

int rotateRight(int movementDirectionPos) {
    return (movementDirectionPos + 1) % 4;
}

array<int, 2> copyIntArray(array<int, 2> oldArray) {
    array<int, 2> newArray;
    for (int i = 0; i < 2; i++) {
        newArray[i] = oldArray[i];
    }
    return newArray;
}

//If it arrives at a same position and rotation as it had before, then it is in a loop
//I didn't realize int arrrays are passed by pionter and not copied... Welp, that's nice to know.
bool isLoop(array<int, 2> currentPosition, vector<string>& obstacleGrid, vector<pair<int, int>> movementDirection, int movementDirectionPos, array<int, 2> newBoxPosition) {

    vector<array<int, 3>> rotationSet;

    if (obstacleGrid[newBoxPosition[0]][newBoxPosition[1]] == '#') {
        return false;
    }
    obstacleGrid[newBoxPosition[0]][newBoxPosition[1]] = '#';
    
    while (true) {

        if (-1 < currentPosition[0] + movementDirection[movementDirectionPos].first
        and currentPosition[0] + movementDirection[movementDirectionPos].first < obstacleGrid.size()
        and -1 < currentPosition[1] + movementDirection[movementDirectionPos].second
        and currentPosition[1] + movementDirection[movementDirectionPos].second < obstacleGrid[0].size()) {
            if (obstacleGrid[currentPosition[0] + movementDirection[movementDirectionPos].first]
            [currentPosition[1] + movementDirection[movementDirectionPos].second] == '#') {
                movementDirectionPos = rotateRight(movementDirectionPos);
                array<int, 3> newRotation = {movementDirectionPos, currentPosition[0], currentPosition[1]};
                for (int i = 0; i < rotationSet.size(); i++) {
                    if (rotationSet[i] == newRotation) {
                        obstacleGrid[newBoxPosition[0]][newBoxPosition[1]] = '.';
                        return true;
                    }
                }
                rotationSet.push_back(newRotation);
            } else {
                currentPosition[0] += movementDirection[movementDirectionPos].first;
                currentPosition[1] += movementDirection[movementDirectionPos].second;
            }
        } else {
            obstacleGrid[newBoxPosition[0]][newBoxPosition[1]] = '.';
            return false;
        }

    }
    obstacleGrid[newBoxPosition[0]][newBoxPosition[1]] = '.';
    return false;
}


int main() {
    ifstream inputFile("AOC6.txt");
    string line;
    vector<string> obstacleGrid;
    array<int, 2> currentPosition;
    //grid[y][x]


    //up, right, down, left
    vector<pair<int, int>> movementDirection = {pair(-1, 0), pair(0, 1), pair(1, 0), pair(0, -1)};
    int movementDirectionPos = 0;

    while (getline(inputFile, line)) {
        obstacleGrid.push_back(line);
    }

    for (int i = 0; i < obstacleGrid.size(); i++) {
        for (int j = 0; j < obstacleGrid[i].size(); j++) {
            if (obstacleGrid[i][j] == '^') {
                currentPosition[0] = i;
                currentPosition[1] = j;
            }
        }
    }

    int total = 0;

    for (int i = 0; i < obstacleGrid.size(); i++) {
        for (int j = 0; j < obstacleGrid[i].size(); j++) {
            //Main check
            array<int, 2> newBoxPosition = {i, j};
            if (isLoop(copyIntArray(currentPosition), obstacleGrid, movementDirection, movementDirectionPos, copyIntArray(newBoxPosition))) {
                total++;
            }
        }
    }



    cout << total;
}