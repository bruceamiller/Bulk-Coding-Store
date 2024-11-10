#include <iostream>

using namespace std;


void Merge(int L[], int R[], int A[], int nL, int nR) {
    int i, j, k;
    i = j = k = 0;
    while (i < nL && j < nR) {
        if (L[i] <= R[j]) {
            A[k] = L[i];
            i++;
        } else {
            A[k] = R[j];
            j++;
        }
        k++;
    }
    while (i < nL) {
        A[k] = L[i];
        i++; k++;
    }
    while (j < nR) {
        A[k] = R[j];
        j++; k++;
    }
}

int main() {
    int L[] = {1, 2, 4, 6};
    int R[] = {3, 5, 7, 8};
    
    int combinedLength = sizeof(L) / sizeof(0) + sizeof(R) / sizeof(0);
    int A[combinedLength];

    Merge(L, R, A, sizeof(L) / sizeof(0), sizeof(R) / sizeof(0));

    for (int i = 0; i < combinedLength; i++) {
        cout << A[i] << " ";
    }
}
