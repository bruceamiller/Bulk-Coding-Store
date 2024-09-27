#include <iostream>
#include <vector>
using namespace std;

int getStepPossibilities(int stepsLeftover, int calculatedSteps[]) {
    if (calculatedSteps[stepsLeftover] != -1) {
        return calculatedSteps[stepsLeftover];
    } else {
        //For calculating big-O notation, consider this next line as one "calculation"
        //Since it doesn't repeat, it should only count each number from 0 -> n once, making the bi-o notation n.
        calculatedSteps[stepsLeftover] = getStepPossibilities(stepsLeftover - 2, calculatedSteps) + getStepPossibilities(stepsLeftover - 1, calculatedSteps);
        return calculatedSteps[stepsLeftover];
    }
}

int main() {
    
    int inputVal;
    cin >> inputVal;
    while (inputVal != 0) {
        int calculatedSteps[inputVal + 1] = {};
        for (int i = 0; i <= inputVal; i++) {
            calculatedSteps[i] = -1;
        }
        calculatedSteps[1] = 1;
        calculatedSteps[2] = 2;
        cout << "Step possibilities: " << getStepPossibilities(inputVal, calculatedSteps) << endl;
        cin >> inputVal;
    }
    return 0;
}

// 11111, 1112, 1121, 1211, 2111, 122, 212, 221
// Number n, how many combinations of 2 & 1 steps?
//n*1 +