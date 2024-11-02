#include <iostream>
#include <algorithm>
using namespace std;



void InsertionSort(int A[], int n) {
    for (int k = 1; k < n; k++) {
        for (int i = 0; i < n - k; i++) {
            if(A[i] > A[i + 1]) {
                swap(A[i], A[i + 1]);
            }
        }
    }
}


int main() {
    int A[] = {2, 7, 4, 1, 5, 3};
    int n = sizeof(A)/sizeof(0);

    InsertionSort(A, n);

    for (int i = 0; i < n; i++) {
        cout << A[i] << " ";
    }

}