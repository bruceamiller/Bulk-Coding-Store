#include <iostream>
#include <vector>
using namespace std;

int getStepPossibilities(int stepsLeftover, int calculatedSteps[]) {
    if (calculatedSteps[stepsLeftover] != -1) {
        return calculatedSteps[stepsLeftover];
    } else {

        calculatedSteps[stepsLeftover] =  getStepPossibilities(stepsLeftover - 1, calculatedSteps) + getStepPossibilities(stepsLeftover - 2, calculatedSteps);
        return calculatedSteps[stepsLeftover];
    }

}
//Assume 1 or 2 are is treated as one step, 1 having 1 possibility, and 2 having two sub-possibilities.
//Every other number  let's say "n" above 1 and 2, splits into  two numbers n-1 and n-2. Since n-1 is calculated first, n-1, n-2, n-3... is calculated all the way down to n = 2.
// This part has n - 1 steps.
// With each of these values stored in the "already calculated array" each of the n - 2's has already been calculated, from n - 2, n-4, n-6... down to 1.
// This part makes n-2 steps.
// If you add n-1 and n-2, you get 2n-3.
// The amount of steps / function calls for each n is (2n - 3). or O(n)

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
// 1111, 211, 121, 112, 22