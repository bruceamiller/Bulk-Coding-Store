#include <iostream>
#include <string>
#include <bits/stdc++.h>
using namespace std;

const int GRID_X = 101;
const int GRID_Y = 103;
const int SECONDS = 100;

//#define DEBUG

void removeChars(istringstream& s, int numRemove) {
    char dumpChar;
    for (int i = 0; i < numRemove; i++) {
        s >> dumpChar;
    }
}

//DEBUG NOTES: Works as intended
int addPositionWithWrappping(int initialPos, int addDist, int wrapSize) {
    initialPos += addDist;
    while (initialPos >= wrapSize) {
        initialPos -= wrapSize;
    }
    while (initialPos < 0) {
        initialPos += wrapSize;
    }
    return initialPos;
}

int main() {
    ifstream inputFile("AOC14.txt");
    string line;
    vector<array<array<int, 2>, 2>> robotsPosAndVelocities;

    int robotGrid[GRID_Y][GRID_X];

    for (int y = 0; y < GRID_Y; y++) {
        for (int x = 0; x < GRID_X; x++) {
            robotGrid[y][x] = 0;
        }
    }

    while (getline(inputFile, line)) {
        istringstream lineStream(line);
        array<array<int, 2>, 2> newPosAndVel;

        removeChars(lineStream, 2);
        lineStream >> newPosAndVel[0][1];
        removeChars(lineStream, 1);
        lineStream >> newPosAndVel[0][0];
        removeChars(lineStream, 2);
        lineStream >> newPosAndVel[1][1];
        removeChars(lineStream, 1);
        lineStream >> newPosAndVel[1][0];

        robotsPosAndVelocities.push_back(newPosAndVel);
    }

    #ifdef DEBUG
    for (array<array<int, 2>, 2> robot : robotsPosAndVelocities) {
        cout << "p=" << robot[0][1] << "," << robot[0][0] << " v=" << robot[1][1] << "," << robot[1][0] << endl;
    }
    for (array<array<int, 2>, 2> robot : robotsPosAndVelocities) {
        robotGrid[robot[0][0]][robot[0][1]] += 1;
    }
    for (int y = 0; y < GRID_Y; y++) {
        for (int x = 0; x < GRID_X; x++) {
            cout << robotGrid[y][x];
        }
        cout << endl;
    }
    cout << endl;
    for (int y = 0; y < GRID_Y; y++) {
        for (int x = 0; x < GRID_X; x++) {
            robotGrid[y][x] = 0;
        }
    }
    #endif


    //Move all robots
    for (int i = 0; i < SECONDS; i++) {
        //Previous issue: If using "for (A : B)" writing to A does not write to B
        for (int i = 0; i < robotsPosAndVelocities.size(); i++) {
            //cout << robot[0][0] << " -> ";
            robotsPosAndVelocities[i][0][0] = addPositionWithWrappping(robotsPosAndVelocities[i][0][0], robotsPosAndVelocities[i][1][0], GRID_Y);
            //cout << robot[0][0] << endl;
            robotsPosAndVelocities[i][0][1] = addPositionWithWrappping(robotsPosAndVelocities[i][0][1], robotsPosAndVelocities[i][1][1], GRID_X);
        }
    }

    //Place robots in grid spaces
    for (array<array<int, 2>, 2> robot : robotsPosAndVelocities) {
        robotGrid[robot[0][0]][robot[0][1]] += 1;
    }

    #ifdef DEBUG
    for (array<array<int, 2>, 2> robot : robotsPosAndVelocities) {
        cout << "p=" << robot[0][1] << "," << robot[0][0] << " v=" << robot[1][1] << "," << robot[1][0] << endl;
    }
    for (int y = 0; y < GRID_Y; y++) {
        for (int x = 0; x < GRID_X; x++) {
            cout << robotGrid[y][x];
        }
        cout << endl;
    }
    #endif

    array<array<array<int, 2>, 2>, 4> quadrantRanges;  //For each {{Ymin, Ymax}, {Xmin, Xmax}}, ...
    quadrantRanges[0][0] = {0, GRID_Y / 2};
    quadrantRanges[0][1] = {GRID_X / 2 + 1, GRID_X};
    quadrantRanges[1][0] = {0, GRID_Y / 2};
    quadrantRanges[1][1] = {0, GRID_X / 2};
    quadrantRanges[2][0] = {GRID_Y / 2 + 1, GRID_Y};
    quadrantRanges[2][1] =  {0, GRID_X / 2};
    quadrantRanges[3][0] = {GRID_Y / 2 + 1, GRID_Y};
    quadrantRanges[3][1] = {GRID_X / 2 + 1, GRID_X};

    #ifdef DEBUG
    cout << "{";
    for (array<array<int, 2>, 2> quadrant : quadrantRanges) {
        cout << "{";
        for (array<int, 2> quadrantCoords : quadrant) {
            cout << "{" << quadrantCoords[0] << "," << quadrantCoords[1] << "}";
        }
        cout << "},";
    }
    cout << "}" << endl;
    #endif

    //Count robots in each quadrant of grid.
    int product = 1;
    for (array<array<int, 2>, 2> quadrant : quadrantRanges) {
        int currentQuadrantTotal = 0;
        for (int y = quadrant[0][0]; y < quadrant[0][1]; y++) {
            for (int x = quadrant[1][0]; x < quadrant[1][1]; x++) {
                currentQuadrantTotal += robotGrid[y][x];                
            }
        }
        product *= currentQuadrantTotal;
    }

    cout << product;

}