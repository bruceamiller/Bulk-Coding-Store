#include <iostream>
#include <algorithm>
using namespace std;



void SelectionSort(int A[], int n) {

    for (int i = 0; i < n-1; i++) {
        int iMin = i;
        for (int j = i + 1; j < n; j++) {
            if (A[j] < A[iMin]) {
                iMin = j;
            }
        }
        swap(A[i], A[iMin]);
    }
}


int main() {
    int A[] = {2, 7, 4, 1, 5, 3};
    int n = sizeof(A)/sizeof(0);

    SelectionSort(A, n);

    for (int i = 0; i < n; i++) {
        cout << A[i] << " ";
    }

}