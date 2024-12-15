#include <iostream>
#include <string>
#include <bits/stdc++.h>
#include <conio.h>
#include <cstdio>
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


void printGrid(array<array<int, GRID_X>, GRID_Y> grid) {
    string gridString;
    for (int y = 0; y < GRID_Y; y++) {
        for (int x = 0; x < GRID_X; x++) {
            if (grid[y][x] == 0) {
                gridString.push_back(' ');
            } else {
                gridString.push_back('1');
            }
            //gridString.push_back(to_string(grid[y][x])[0]);
        }
        gridString.push_back('\n');
    }
    cout << gridString;
}

/*
void printGrid(array<array<int, GRID_X>, GRID_Y> grid) {
    char charGrid[(GRID_Y+1)*GRID_X];
    for (int y = 0; y < GRID_Y; y++) {
        for (int x = 0; x < GRID_X; x++) {
            if (grid[y][x] == 0) {
                charGrid[y * (GRID_Y + 1) + x] = ' ';
            } else {
                charGrid[y * (GRID_Y + 1) + x] = '1';
            }
        }
        charGrid[(y + 1) * (GRID_Y + 1) - 1] = '\n';
    }
    for (int i = 0; i < (GRID_Y+1)*GRID_X; i++) {
        cout << charGrid[i];
    }
    //printf("%s", charGrid.c_str(););
}
*/

void eraseGrid(array<array<int, GRID_X>, GRID_Y>& grid) {
    for (int y = 0; y < GRID_Y; y++) {
        for (int x = 0; x < GRID_X; x++) {
            grid[y][x] = 0;
        }
    }
}

int main() {
    ifstream inputFile("AOC14.txt");
    string line;
    vector<array<array<int, 2>, 2>> robotsPosAndVelocities;

    array<array<int, GRID_X>, GRID_Y> robotGrid;

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

    //Moving the graph individually, I noticed that there are horizontal lines at 50 + 103A and 95 + 101B for some integers A & B currentSeconds, so I'm going to find the intercept.
    

    int currentSeconds = 100;
    /*
    cout << "Skip to: ";
    cin >> currentSeconds;
    */
    while (!((currentSeconds - 50) % 103 == 0) or !((currentSeconds - 95) % 101 == 0)) {
        currentSeconds++;
    }
    

    

    for (int j = 0; j < currentSeconds; j++) {
        for (int i = 0; i < robotsPosAndVelocities.size(); i++) {
            //cout << robot[0][0] << " -> ";
            robotsPosAndVelocities[i][0][0] = addPositionWithWrappping(robotsPosAndVelocities[i][0][0], robotsPosAndVelocities[i][1][0], GRID_Y);
            //cout << robot[0][0] << endl;
            robotsPosAndVelocities[i][0][1] = addPositionWithWrappping(robotsPosAndVelocities[i][0][1], robotsPosAndVelocities[i][1][1], GRID_X);
        }
    }



    //Move all robots
    string inputString;
    char input;
    input = _getch();
    while (input != 27) {
        system("cls");
        cout << "Seconds: " << currentSeconds << endl << endl;
        for (array<array<int, 2>, 2> robot : robotsPosAndVelocities) {
            robotGrid[robot[0][0]][robot[0][1]] += 1;
        }
        printGrid(robotGrid);
        eraseGrid(robotGrid);
        cout << endl;
        input = _getch();
        if (input == 'n') {
            for (int i = 0; i < robotsPosAndVelocities.size(); i++) {
                //cout << robot[0][0] << " -> ";
                robotsPosAndVelocities[i][0][0] = addPositionWithWrappping(robotsPosAndVelocities[i][0][0], robotsPosAndVelocities[i][1][0], GRID_Y);
                //cout << robot[0][0] << endl;
                robotsPosAndVelocities[i][0][1] = addPositionWithWrappping(robotsPosAndVelocities[i][0][1], robotsPosAndVelocities[i][1][1], GRID_X);
            }
            currentSeconds++;
        } else if (input == 'b') {
            for (int i = 0; i < robotsPosAndVelocities.size(); i++) {
                //cout << robot[0][0] << " -> ";
                robotsPosAndVelocities[i][0][0] = addPositionWithWrappping(robotsPosAndVelocities[i][0][0], -robotsPosAndVelocities[i][1][0], GRID_Y);
                //cout << robot[0][0] << endl;
                robotsPosAndVelocities[i][0][1] = addPositionWithWrappping(robotsPosAndVelocities[i][0][1], -robotsPosAndVelocities[i][1][1], GRID_X);
            }
            currentSeconds--;
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

}