#include <iostream>

using namespace std;

int main() {
    int inputVal = 0;
    int intStore[10] = {};
    int intStorePos = 0;
    int doubles = 0;

    bool newArray = false;
    cin >> inputVal;
    while (inputVal != -1) {
        if (newArray) {
            for (int i = 0; i <= 10; i++) {
                intStore[i] = 0;
            }
            intStorePos = 0;
            doubles = 0;
            newArray = false;
            cin >> inputVal;
        }
        if (inputVal == 0) {
            int currentNumberPos = 0;
            int currentNumberChecking = intStore[currentNumberPos];
            while (currentNumberChecking != 0) {
                for (int i = 0; i <= 10; i++) {
                    if (currentNumberChecking / 2.0 == intStore[i]) {
                        doubles += 1;
                    }
                }
                currentNumberPos++;
                currentNumberChecking = intStore[currentNumberPos];
            }
            /*
            cout << "List: ";
            for (int i = 0; i <= 10; i++) {
                cout  << intStore[i] << " ";
            }
            cout << "|" << doubles << endl;
            newArray = true;
            */
        } else {
            intStore[intStorePos] = inputVal;
            intStorePos += 1;
            cin >> inputVal;
        }
    }
}