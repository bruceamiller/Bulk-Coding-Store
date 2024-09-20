#include <iostream>
using namespace std;

void printArray(int *ptr, int size) {
    for (int i = 0; i < size; i++) {
        cout << *ptr++ << " ";
    }
}

int main() {
    int *ptr = new int[5] {1, 3, 5, 7, 9};
    cout << *(ptr + 1);
    // printArray(arr, 5);

    return 0;
}