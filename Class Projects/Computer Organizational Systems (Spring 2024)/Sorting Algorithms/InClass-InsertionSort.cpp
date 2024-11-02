#include <iostream>
#include <algorithm>
using namespace std;


void InsertionSort(int A[], int n) {
    for (int i = 1; i < n; i++) {
        int value = A[i];
        int hole = i;
        while (hole > 0 && A[hole-1] > value) {
            A[hole] = A[hole-1];
            hole = hole-1;
        }
        A[hole] = value;
    }
}


int main() {
    int A[] = {90, 17, 88, 22, 5, 82};
    int n = sizeof(A)/sizeof(0);

    InsertionSort(A, n);

    for (int i = 0; i < n; i++) {
        cout << A[i] << " ";
    }

}