#include <iostream>
#include <string>
#include <cstdlib>
#include <ctime>

using namespace std;

//#define DEBUG

//Check if one string is a prefix of the next;
bool isPrefix(string a, string b) {
    if (a.size() > b.size()) return false;
    return b.substr(0, a.size()) == a;
}


void QuickSort(string array[], int length);
void QuickSortRecursion(string array[], int low, int high);
int RandomizedParition(string array[], int low, int high);

//Sorting stuff:
void QuickSort(string array[], int length) {
    srand(time(nullptr));
    QuickSortRecursion(array, 0, length - 1);
}

void QuickSortRecursion(string array[], int low, int high) {
    if (low < high) {

        int pivotIndex = RandomizedParition(array, low, high);
        QuickSortRecursion(array, low, pivotIndex -1);
        QuickSortRecursion(array, pivotIndex + 1, high);       
    }
}

int RandomizedParition(string array[], int low, int high) {
    int randomPivotIndex = low + rand() % (high - low + 1);
    if (randomPivotIndex != high) {
        swap(array[randomPivotIndex], array[high]);
    }
    string pivotValue = array[high];
    int pivotIndex = low;
    for (int j = low; j < high; j++) {
        if (array[j] <= pivotValue) {
            swap(array[pivotIndex], array[j]);
            pivotIndex++;
        }
    }
    swap(array[pivotIndex], array[high]);
    return pivotIndex;
}


int main() {
    string stringList[40];
    string currentString;
    int currentStringPos = 0;

    // Get list of strings
    //End string list by inputting forty number strings, or inputting invalid number "-1"
    cin >> currentString;
    while (currentStringPos < 40 and currentString != "-1") {
        #ifdef debug
        cout << currentString << endl;
        #endif
        stringList[currentStringPos] = currentString;
        currentStringPos++;
        cin >> currentString;
        
    }

    QuickSort(stringList, currentStringPos + 1);

    #ifdef DEBUG

    cout << "Sorted list:" << endl;

    for (int i = 0; i < currentStringPos + 1; i++) {
        cout << stringList[i] << endl;
    }

    #endif

    //Compare sorted strings
    for (int i = 0; i < currentStringPos; i++) {
        if (isPrefix(stringList[i], stringList[i + 1])) {
            cout << "No" << endl;
            return 0;
        }
    }
    cout << "Yes" << endl;
    return 0;
}
