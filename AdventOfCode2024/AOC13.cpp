#include <iostream>
#include <string>
#include <bits/stdc++.h>
using namespace std;

//#define DEBUG

bool charInString(char c, string s) {
    for (int i = 0; i < s.size(); i++) {
        if (s[i] == c) {
            return true;
        }
    }
    return false;
}

array<int, 2> getStringNumPairs(string s) {
    string nums = "0123456789";
    string numsOnly;
    for (int i = 0; i < s.size(); i++) {
        if (charInString(s[i], nums)) {
            numsOnly.push_back(s[i]);
        } else {
            numsOnly.push_back(' ');
        }
    }
    istringstream numsOnlyStream(numsOnly);
    array<int, 2> outputNums;
    numsOnlyStream >> outputNums[0] >> outputNums[1];
    #ifdef DEBUG
        cout << outputNums[0] << " " << outputNums[1] << endl;
    #endif
    return outputNums;
}

bool matchesPosition(vector<pair<array<int, 2>, int>> buttonPairsAndPresses, array<int, 2> prizePair ) {
    for (pair<array<int, 2>, int> pairPosAndPresses : buttonPairsAndPresses) {
        prizePair[0] -= pairPosAndPresses.first[0] * pairPosAndPresses.second;
        prizePair[1] -= pairPosAndPresses.first[1] * pairPosAndPresses.second;
    }
    array<int, 2> emptyPair = {0, 0};
    if (prizePair == emptyPair) {
        return true;
    }
    return false;
}

int getCost(vector<array<int, 2>> buttonPressesAndCosts) {
    int total = 0;
    for (array<int, 2> buttonPressAndCost : buttonPressesAndCosts) {
        total += buttonPressAndCost[0] * buttonPressAndCost[1]; 
    }
    return total;
}

bool partiallyGreaterThanOrEqual(vector<pair<array<int, 2>, int>> buttonPairsAndPresses, array<int, 2> prizePair ) {
    for (pair<array<int, 2>, int> pairPosAndPresses : buttonPairsAndPresses) {
        prizePair[0] -= pairPosAndPresses.first[0] * pairPosAndPresses.second;
        prizePair[1] -= pairPosAndPresses.first[1] * pairPosAndPresses.second;
    }
    array<int, 2> emptyPair = {0, 0};
    if (prizePair[0] <= 0 or prizePair[1] <= 0) {
        return true;
    }
    return false;
}

int getMinimumPrice(array<int, 2> buttonAPair, array<int, 2> buttonBPair, array<int, 2> prizePair) {
    int aPrice = 3;
    int bPrice = 1;

    //Set A just a bit larger than the prizePos, or equal.
    int buttonAPresses = min(ceil(float(prizePair[0]) / float(buttonAPair[0])), ceil(float(prizePair[1]) / float(buttonAPair[1])));
    int buttonBPresses = 0;


    int currentCheapestCost = -1;
    
    //Reduce A size until less than prize pair, or 0.
    //Then, increase ButtonB pair until matches prize pair, or higher.
    while (buttonAPresses > -1) {
        //If match save in list.
        if (matchesPosition({pair(buttonAPair, buttonAPresses), pair(buttonBPair, buttonBPresses)}, prizePair)) {
            int currentPrice = getCost({{buttonAPresses, aPrice}, {buttonBPresses, bPrice}});
            if (currentCheapestCost == -1 or currentPrice < currentCheapestCost) {
                cout << buttonAPresses << " - " << buttonBPresses << " - " << currentPrice << endl;
                currentCheapestCost = currentPrice;
            }
        }
        buttonAPresses--;
        while (!partiallyGreaterThanOrEqual({pair(buttonAPair, buttonAPresses), pair(buttonBPair, buttonBPresses)}, prizePair)) {
            buttonBPresses++;
        }
    }

    //Compare all prices of matches in list, to see which is better.
    if (currentCheapestCost != -1) {
        return currentCheapestCost;
    }
    return 0;
}


int main() {
    ifstream inputFile("AOC13.txt");
    string line;
    vector<array<int, 2>> buttonAPairs;
    vector<array<int, 2>> buttonBPairs;
    vector<array<int, 2>> prizePairs;

    
    while (getline(inputFile, line)) {
        getline(inputFile, line);
        buttonAPairs.push_back(getStringNumPairs(line));
        getline(inputFile, line);
        buttonBPairs.push_back(getStringNumPairs(line));
        getline(inputFile, line);
        prizePairs.push_back(getStringNumPairs(line));
        #ifdef DEBUG
            cout << endl;
        #endif
    }

    int total = 0;

    for (int i = 0; i < prizePairs.size(); i++) {
        total += getMinimumPrice(buttonAPairs[i], buttonBPairs[i], prizePairs[i]);
    }

    cout << total;



    return 0;
}

/*
        array<int, 2> newPrizePair = getStringNumPairs(line);
        newPrizePair[0] += 10000000000000;
        newPrizePair[1] += 10000000000000;
        prizePairs.push_back(newPrizePair);
*/