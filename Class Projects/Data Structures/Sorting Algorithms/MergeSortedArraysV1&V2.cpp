#include <iostream>

using namespace std;

void MergeSort(int array[], int length);
void MergeSortRecursion(int array[], int l, int r);
void MergeSortedArraysV1 (int array[], int l, int m, int r);
void MergeSortedArraysV2 (int array[], int l, int m, int r);

void MergeSort(int array[], int length) {
    MergeSortRecursion(array, 0, length-1);
}

void MergeSortRecursion(int array[], int l, int r) {
    if (l < r) {
        int m = l + (r - l) / 2;
        
        MergeSortRecursion(array, l, m);
        MergeSortRecursion(array, m + 1, r);
        //MergeSortedArraysV1(array, l, m, r);
        MergeSortedArraysV2(array, l, m, r);

    }
}

void MergeSortedArraysV1(int array[], int l, int m, int r) {
    int leftSize = m - l + 1;
    int rightSize = r - m;

    int leftArray[leftSize];
    int rightArray[rightSize];


    for (int i = 0; i < leftSize; i++) {
        leftArray[i] = array[l + i];
    }

    for (int j = 0; j < rightSize; j++) {
        rightArray[j] = array[m + 1 + j];
    }

    int i = 0, j = 0, k = l;

    while (i < leftSize && j < rightSize) {
        if (leftArray[i] <= rightArray[j]) {
            array[k] = leftArray[i];
            i++;
        } else {
            array[k] = rightArray[j];
            j++;
        }
        k++;
    }

    while (i < leftSize) {
        array[k] = leftArray[i];
        i++;
        k++;
    }

    while (j < rightSize) {
        array[k] = rightArray[j];
        j++;
        k++;
    }


}

void MergeSortedArraysV2(int array[], int l, int m, int r) {
    int leftSize = m - l + 1;
    int rightSize = r - m;

    int leftArray[leftSize];
    int rightArray[rightSize];


    for (int i = 0; i < leftSize; i++) {
        leftArray[i] = array[l + i];
    }

    for (int j = 0; j < rightSize; j++) {
        rightArray[j] = array[m + 1 + j];
    }
 
    int i , j , k ;

    for (i = 0, j = 0, k = l; k <= r; k++) {
        if ( (i < leftSize) && (j >= rightSize || leftArray[i] <= rightArray[j]) ) {
            array[k] = leftArray[i];
            i++;
        } else {
            array[k] = rightArray[j];
            j++;
        }
    }
}

int main() {
    int A[] = {7, 2, 1, 6, 8, 5, 3, 4};
    int length = 8;
    
    MergeSort(A, length);


    for (int i = 0; i < length; i++) {
        cout << A[i] << " ";
    }
    cout << endl;

    return 0;
}