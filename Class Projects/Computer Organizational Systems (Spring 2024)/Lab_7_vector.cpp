//#include <stack> // Changing these positions fixed bug stack undefined
#include <vector>
#include <iostream>
using namespace std;

int main() {
    vector<string> outputVector;
    string currentString;
    int setNumber = 0;
    int stackSize;
    cin >> stackSize;
    while (stackSize != 0) {
        setNumber++;
        cout << "SET " << setNumber << endl;
        for (int i = 0; i < stackSize; i++) {
            cin >> currentString;
            if (i % 2 == 0) {
                cout << currentString << " ";
            } else {
                outputVector.push_back(currentString);
            }
        }
        for (int i = 0; i < stackSize - stackSize / 2; i++) {
            cout << outputVector.back() << " ";
            outputVector.pop_back();
        }
        cout << endl;
        cin >> stackSize;
    }
    
    return 0;
}