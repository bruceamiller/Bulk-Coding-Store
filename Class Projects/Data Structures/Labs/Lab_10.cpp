#include <iostream>
#include <string>

using namespace std;

int getHeightRecursive(string treeInput, int pos);

int getHeight(string treeInput) {
    return getHeightRecursive(treeInput, 0);
}

int getHeightRecursive(string treeInput, int pos) {
    int currentDepth = 1;
    int maxDepth = 1;
    int nextMaxDepth;
    pos++;
    while (currentDepth > 0 and pos < treeInput.size()) {
        if (treeInput[pos] == 'd') {
            currentDepth++;
        } else if (treeInput[pos] == 'u') {
            currentDepth--;
        }
        if (currentDepth > maxDepth) {
            maxDepth = currentDepth;
        }
        pos++;
    }
    if (pos < treeInput.size()) {
        nextMaxDepth = getHeightRecursive(treeInput, pos);
        if (nextMaxDepth > maxDepth) {
            return nextMaxDepth;
        } else {return maxDepth;}
    }
    return maxDepth;
}


int main() {
    string inputString;
    int currentTree = 1;

    cin >> inputString;
    while (inputString != "#") {
        cout << "Tree " << currentTree << ": " << getHeight(inputString) << endl;
        currentTree++;
        cin >> inputString;
    }
}