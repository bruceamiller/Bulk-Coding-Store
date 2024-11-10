#include <iostream>
#include <vector>
#include <string>
using namespace std;

//#define DEBUG

bool customerInGroup(vector<char> customers, char newCustomer) {
    for (int i = 0; i < customers.size(); i++) {
        if (customers[i] == newCustomer) return true;
    }
    return false;
}

bool positionInGroup(vector<char> customers, char newCustomer) {
        for (int i = 0; i < customers.size(); i++) {
        if (customers[i] == newCustomer) return i;
    }
    return -1;
}

bool isLetter(char newCustomer) {
    string letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    for (int i = 0; i < letters.size(); i++) {
        if (letters[i] == newCustomer) return true;
    }
    return false;
}

int main() {    
    vector<char> currentlyTanning;
    vector<char> alreadyProcessed;
    int totalTanning;
    int walkedAway;

    int tanningBeds;
    string peopleInput;

    cin >> tanningBeds;
    while (tanningBeds != 0) {
        totalTanning = 0;
        walkedAway = 0;
        currentlyTanning.erase(currentlyTanning.begin(), currentlyTanning.end());
        alreadyProcessed.erase(currentlyTanning.begin(), currentlyTanning.end());
        cin >> peopleInput;
        #ifdef DEBUG
            cout << "|" << tanningBeds << "|" << peopleInput << endl;
        #endif
        for (int i = 0; i < peopleInput.size(); i++) {

            if (customerInGroup(currentlyTanning, peopleInput[i])) { //Customer is tanning already
                auto deletePos = currentlyTanning.begin() + positionInGroup(currentlyTanning, peopleInput[i]);
                currentlyTanning.erase(deletePos);
                totalTanning -= 1;
            } else if (customerInGroup(alreadyProcessed, peopleInput[i])) { //Customer is not tanning and has already been processed.
            } else { //Customer is not tanning and has not been processed.
                if (totalTanning < tanningBeds) { // If room, start tanning
                    currentlyTanning.push_back(peopleInput[i]);
                    totalTanning++;
                } else { // if not room walk away.
                    alreadyProcessed.push_back(peopleInput[i]);
                    walkedAway++;
                }
            }
        }
        cout << walkedAway << endl;
        cin >> tanningBeds;
    }

    return 0;
}



/*
2 CBALLMMACZBDDZ (3 customer(s) walked away.)
5 VWXYZWVXYZABCDEFFABCDE (1 customer(s) walked away.)	
0
*/

