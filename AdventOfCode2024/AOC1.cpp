#include <iostream>
#include <bits/stdc++.h>
#include <string>
#include <sstream>
#include <cmath>
using namespace std;

void MergeSort(vector<int>& array);
void MergeSortRecursion(vector<int>& array, int l, int r);
void MergeSortedArraysV1 (vector<int>& array, int l, int m, int r);

int main() {
    ifstream inputFile("AOC1.txt");
    string inputString;

    vector<int> leftList;
    vector<int> rightList;

    int newLeft;
    int newRight;

    //Get all values
    while (getline(inputFile, inputString)) {
        istringstream inputStream(inputString);
        inputStream >> newLeft >> newRight;
        leftList.push_back(newLeft);
        rightList.push_back(newRight);
    }

    //Sort values in both lists
    MergeSort(leftList);
    MergeSort(rightList);

    //Compare both lists
    int sum = 0;
    for (int i = 0; i < leftList.size(); i++)
        sum += abs(rightList[i] - leftList[i]); // Absolute value, might need fix?
    cout << sum;

    return 0;
}


void MergeSort(vector<int>& array) {
    int length = array.size();
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