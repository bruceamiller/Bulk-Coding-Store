#include <iostream>
#include <vector>

using namespace std;

void MergeSort(vector<int>& array, int length);
void MergeSortRecursion(vector<int>& array, int l, int r);
void MergeSortedArraysV1 (vector<int>& array, int l, int m, int r);

void MergeSort(vector<int>& array, int length) {
    MergeSortRecursion(array, 0, length-1);
}

void MergeSortRecursion(vector<int>& array, int l, int r) {
    if (l < r) {
        int m = l + (r - l) / 2;
        
        MergeSortRecursion(array, l, m);
        MergeSortRecursion(array, m + 1, r);
        MergeSortedArraysV1(array, l, m, r);
    }
}

void MergeSortedArraysV1(vector<int>& array, int l, int m, int r) {
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

int main() {
    vector<int> A = {7, 2, 1, 6, 8, 5, 3, 4};
    int length = A.size();

    MergeSort(A, length);


    for (int i = 0; i < length; i++) {
        cout << A[i] << " ";
    }
    cout << endl;

    return 0;
}