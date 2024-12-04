#include <iostream>
#include <bits/stdc++.h>
#include <string>
#include <sstream>
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

    int total = 0;
    for (int i = 0; i < leftList.size(); i++)
        total += leftList[i] * count(rightList.begin(), rightList.end(), leftList[i]);
    cout << total;
    return 0;
}