#include <iostream>
#include <bits/stdc++.h>
#include <string>
#include <vector>
using namespace std;

int rotateRight(int movementDirectionPos) {
    return (movementDirectionPos + 1) % 4;
}

int main() {
    ifstream inputFile("AOC6.txt");
    string line;
    vector<string> obstacleGrid;
    int currentPosition[2];
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

    while(-1 < currentPosition[0] and currentPosition[0] < obstacleGrid.size() and -1 < currentPosition[1] and currentPosition[1] < obstacleGrid[0].size()) {
        obstacleGrid[currentPosition[0]][currentPosition[1]] = 'X';
        
        //If next move is box, then rotate movement right.

        while (-1 < currentPosition[0] + movementDirection[movementDirectionPos].first
        and currentPosition[0] + movementDirection[movementDirectionPos].first < obstacleGrid.size()
        and -1 < currentPosition[1] + movementDirection[movementDirectionPos].second
        and currentPosition[1] + movementDirection[movementDirectionPos].second < obstacleGrid[0].size()
        and obstacleGrid[currentPosition[0] + movementDirection[movementDirectionPos].first]
        [currentPosition[1] + movementDirection[movementDirectionPos].second] == '#') {
            movementDirectionPos = rotateRight(movementDirectionPos);
        }


        currentPosition[0] += movementDirection[movementDirectionPos].first;
        currentPosition[1] += movementDirection[movementDirectionPos].second;
    }

    int total = 0;
    for (int i = 0; i < obstacleGrid.size(); i++) {
        for (int j = 0; j < obstacleGrid[i].size(); j++) {
            if (obstacleGrid[i][j] == 'X') {
                total++;
            }
        }
    }

    cout << total;
}
