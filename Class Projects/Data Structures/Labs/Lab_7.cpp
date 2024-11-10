#include <stack> // Changing these positions fixed bug stack undefined
#include <iostream>
using namespace std;

int main() {
    stack<string> outputStack;
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
                outputStack.push(currentString);
            }
        }
        for (int i = 0; i < stackSize - stackSize / 2; i++) {
            cout << outputStack.top() << " ";
            outputStack.pop();
        }
        cout << endl;
        cin >> stackSize;
    }
    
    return 0;
}