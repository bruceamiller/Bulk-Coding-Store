#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;


void QuickSort(int array[], int length);
void QuickSortRecursion(int array[], int low, int high);
int RandomizedParition(int array[], int low, int high);

void QuickSort(int array[], int length) {
    srand(time(nullptr));
    QuickSortRecursion(array, 0, length - 1);
}

void QuickSortRecursion(int array[], int low, int high) {
    if (low < high) {

        int pivotIndex = RandomizedParition(array, low, high);
        QuickSortRecursion(array, low, pivotIndex -1);
        QuickSortRecursion(array, pivotIndex + 1, high);       
    }
}

int RandomizedParition(int array[], int low, int high) {
    int randomPivotIndex = low + rand() % (high - low + 1);
    if (randomPivotIndex != high) {
        swap(array[randomPivotIndex], array[high]);
    }
    int pivotValue = array[high];
    int pivotIndex = low;
    for (int j = low; j < high; j++) {
        if (array[j] <= pivotValue) { // Change to >= for descending order
            swap(array[pivotIndex], array[j]);
            pivotIndex++;
        }
    }
    swap(array[pivotIndex], array[high]);
    return pivotIndex;
}

int main() {
    int A[] = {2, 7, 1, 6, 8, 5, 3, 4};
    int length = sizeof(A)/sizeof(0);

    QuickSort(A, length);

    for (int i = 0; i < length; i++) {
        cout << A[i] << " ";
    }

    return 0;
}

//Pivot debugging:
// [2, 7, 1, 6, 8, 5, 3, 4]
// low = 0, high = 6, pivotValue = 4, pivotIndex = 0
// j = 0
// swap(array[0], array[0]) [2, 7, 1, 6, 8, 5, 3, 4]
// pivotIndex = 1
// j = 1
// j = 2
// swap(array[1], array[2]) [2, 1, 7, 6, 8, 5, 3, 4]
// pivotIndex = 2;
// j = 3
// j = 4
// j = 5
// j = 6
// swap(array[2], array[6]) [2, 1, 3, 6, 8, 5, 7, 4]
// pivotIndex = 3;
// swap(array[3], array[7])
// [2, 1, 3, 4, 8, 5, 7, 6]
// Okay, so you're going through and swapping low numbers towards the beginning.
// It's also weird because low numbers can swap with themselves if a big number hasn't been found yet.
// If numbers are bigger, you leave them, because you can swap a smaller number with them later.
// Then you swap the partition with one of those bigger numbers.