#include <iostream>
using namespace std;

int getStepPossibilities(int stepsLeftover) {
    if (stepsLeftover == 1) {
        return 1;
    } else if (stepsLeftover == 2) {
        return 1 + getStepPossibilities(1); //One version is stepsLeftover -- 2, the next is stepsLeftover - 1
    } else {
        return getStepPossibilities(stepsLeftover - 2) + getStepPossibilities(stepsLeftover - 1);
    }
}

int main() {
    int inputVal;
    cin >> inputVal;
    while (inputVal != 0) {
        cout << "Step possibilities: " << getStepPossibilities(inputVal) << endl;
        cin >> inputVal;
    }
    return 0;
}

// 11111, 1112, 1121, 1211, 2111, 122, 212, 221