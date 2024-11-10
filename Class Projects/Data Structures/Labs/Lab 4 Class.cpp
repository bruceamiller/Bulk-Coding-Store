#include <iostream>

// #define DEBUG

using namespace std;

class inputList {
    public:

        void printArray() {
            cout << "List: ";
            for (int i = 0; i <= 10; i++) {
                cout  << intStore[i] << " ";
            }
            cout << "| ";
        };

        void addValueToArray(int inputVal) {
            intStore[intStorePos] = inputVal;
            intStorePos += 1;
        }

        int getDoubles() {
            int doubles;
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
            return doubles;
        };

    private:
        int intStore[10] = {};
        int intStorePos = 0;
};

int main() {
    int inputVal = 0;
    inputList inputsStore;

    cin >> inputVal;
    while (inputVal != -1) {
        if (inputVal == 0) {
            #ifdef DEBUG
                inputsStore.printArray();
            #endif
            cout << inputsStore.getDoubles() << endl;
            inputsStore = inputList();
        } else {
            inputsStore.addValueToArray(inputVal);
        }
        cin >> inputVal;
    }
}
