#include <iostream>
#include <vector>
using namespace std;

//(for) loop only runs once per array value, making it O(n).
//Since 1 and 2 are pre-calculated you could say O(n) = n - 2
int main() {
    
    int inputVal;
    cin >> inputVal;
    while (inputVal != 0) {
        int calculatedSteps[inputVal + 1] = {};
        calculatedSteps[1] = 1;
        calculatedSteps[2] = 2;
        for (int i = 3; i <= inputVal; i++) {
            calculatedSteps[i] = calculatedSteps[i - 2] + calculatedSteps[i - 1];
        }

        cout << "Step possibilities: " << calculatedSteps[inputVal] << endl;
        cin >> inputVal;
    }
    return 0;
}