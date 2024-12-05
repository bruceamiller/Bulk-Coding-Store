#include <iostream>
#include <bits/stdc++.h>
#include <string>
#include <vector>
using namespace std;

//#define DEBUG



bool charInString(char c, string s) {
    for (int i = 0; i < s.size(); i++) {
        if (s[i] == c)
            return true;
    }
    return false;
}

int rightValueFirstPairPos(int val, vector<pair<int, int>> pairs) {
    for (int i = 0; i < pairs.size(); i++) {
        if (pairs[i].second == val)
            return i;
    }
    return -1;
}

bool numInList(int val, vector<int> intList) {
    for (int i = 0; i < intList.size(); i++) {
        if (intList[i] == val) {
            return true;
        }
    }
    return false;
}



int main() {
    ifstream inputFile("AOC5.txt");
    string line;
    vector<pair<int, int>> pagePairings;
    vector<vector<int>> pageOrderLists;

    //Get all pairs and all lines.
    while (getline(inputFile, line)) {
        char dumpChar;
        istringstream currentLineStream(line);
        if (charInString('|', line)) {
            int pairA, pairB;
            
            currentLineStream >> pairA >> dumpChar >> pairB;
            pagePairings.push_back(pair(pairA, pairB));
        } else if (charInString(',', line)) {
            vector<int> currentLineOrder;
            int currentLineVal;
            currentLineStream >> currentLineVal;
            currentLineOrder.push_back(currentLineVal);
            while (currentLineStream >> dumpChar) {
                currentLineStream >> currentLineVal;
                currentLineOrder.push_back(currentLineVal);
            }
            pageOrderLists.push_back(currentLineOrder);
        }
    }

    #ifdef DEBUG
    for (int i = 0; i < pagePairings.size(); i++) {
        cout << pagePairings[i].first << "|" << pagePairings[i].second << endl;
    }
    cout << endl;

    for (int i = 0; i < pageOrderLists.size(); i++) {
        for (int j = 0; j < pageOrderLists[i].size(); j++) {
            cout << pageOrderLists[i][j] << ",";
        }
        cout << endl;
    }
    cout << endl;
    #endif
    
    
    //Make list of each left number in a pair, with all of its various right numbers.
    vector<pair<int, vector<int>>> allRightsPerLeftPair;

    for (int i = 0;  i < pagePairings.size(); i++) {
        bool isLeftPair = false;
        for (int j = 0; j < allRightsPerLeftPair.size(); j++) {
            if (pagePairings[i].first == allRightsPerLeftPair[j].first) {
                isLeftPair = true;
                allRightsPerLeftPair[j].second.push_back(pagePairings[i].second);
                break;
            }
        }
        if (!isLeftPair) {
            vector<int> secondInPairVec = {pagePairings[i].second};
            allRightsPerLeftPair.push_back(pair(pagePairings[i].first, secondInPairVec));
        }
    }
    
    int total = 0;
    //Go through each pageOrderList at the end and check each page, seeing if the page to the right in the array fit the potential right pair page number for each left.
    //I Guess this isn't checking both directions? Need to fix.
    for (int i = 0; i < pageOrderLists.size(); i++) { // i ==  current page order
        for (int j = 0; j < pageOrderLists[i].size(); j++) { //j == current letter left being checked
            int pageLeftPos;
            bool validLetter = true;
            for (int k = j + 1; k < pageOrderLists[i].size(); k++) { // letter right being checked.
                //Find the second page
                for (int a = 0; a < allRightsPerLeftPair.size(); a++) {
                    if (allRightsPerLeftPair[a].first == pageOrderLists[i][k]) {
                        pageLeftPos = a;
                        break;
                    }
            }
            
            //Check if the current page being checked is supposed to be after and not before.
            if (numInList(pageOrderLists[i][j], allRightsPerLeftPair[pageLeftPos].second)) {
                validLetter = false;
                break;
            }
            }
            if (validLetter == false) {
                break;
            } else if (j == pageOrderLists[i].size() - 1) {
                total += pageOrderLists[i][pageOrderLists[i].size() / 2];
            }
        }
    }

    cout << total;
    

    return 0;
}

    //Insert all pairs into a sorted array with all values.
    //Insert first pair int o list, left, right, 0, 1

    //Check the first value in list and see if there is a number before it.
    //If there is a pair with the searched value on the right, and the left number isn't already in the list:
    // insert a new value to the left of the current pos and make that the new pos
    //When there is no value right of pos becomes pos.
    //When pos reaches the end, insert the first pair at the end, and continue.

    //Values can be limited to only certain books. May not overlap perfectly, making this obsolete.
    /*
    vector<int> totalSorted;
    totalSorted.push_back(pagePairings[0].first);
    totalSorted.push_back(pagePairings[0].second);
    pagePairings.erase(pagePairings.begin());

    for (int i = 0; i < totalSorted.size(); i++) {
        int nextPairingPos = rightValueFirstPairPos(totalSorted[i], pagePairings);
        if (nextPairingPos != -1) { //If there is a pair value to the left of this number
            if (!numInList(pagePairings[nextPairingPos].first, totalSorted)){// and the pair on left is not already in list, add it, otherwise remove it.
                totalSorted.insert(totalSorted.begin() + i, pagePairings[nextPairingPos].first);
            }
            pagePairings.erase(pagePairings.begin() + nextPairingPos);
            i--;
        }
        if (i == totalSorted.size() - 1 and i != -1 and pagePairings.size() > 0) { //If you reach the end of sorted list, but still need to add more pairs.
            totalSorted.push_back(pagePairings[0].first);
            totalSorted.push_back(pagePairings[0].second);
            pagePairings.erase(pagePairings.begin());
        }
    }
    
    
    #ifdef DEBUG
    for (int i = 0; i < totalSorted.size(); i++) {
        cout << totalSorted[i] << " ";
    }
    cout << endl;
    #endif

    //Check each end array with all sorted arrays. And add central value if valid.
    int total = 0;
    for (int list; list < pageOrderLists.size(); list++) {
            int currentLeftmost = 0;
        for (int i = 0; i < pageOrderLists[list].size(); i++) { // For each page in order list being checked
            while(pageOrderLists[list][i] != totalSorted[currentLeftmost] and currentLeftmost < totalSorted.size()) { //Find if the current value is within the list being checked, and move position over when found
                currentLeftmost++;
            }
            if (currentLeftmost == totalSorted.size() and i < pageOrderLists[list].size()) { //If position reaches end of sorted list, before all values are found in the list being checked, then break
                break;
            } else if (currentLeftmost != totalSorted.size() and i < pageOrderLists[list].size() - 1) {
            } else {
                total += pageOrderLists[list][pageOrderLists[list].size() / 2];
                break;
            }
        }
    }
    */
