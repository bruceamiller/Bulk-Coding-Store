#include <iostream>
#include <string>
using namespace std;

int main() {
    string *strPtr = new string("Hello World");

    cout << "Length of the string: " << strPtr -> length() << endl;
    cout << "Length of the string: " << (*strPtr).length() << endl;

    delete strPtr;

    return 0;
}