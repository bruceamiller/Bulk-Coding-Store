#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> myIntVector;
    vector<int>::iterator it;

    for (int i = 1; i <= 5; i++) myIntVector.push_back(i);

    cout << "myVector contains: " ;
    for (it = myIntVector.begin(); it != myIntVector.end(); it++) {
        cout << *it << " ";
    }
    cout << endl;

    return 0;

}