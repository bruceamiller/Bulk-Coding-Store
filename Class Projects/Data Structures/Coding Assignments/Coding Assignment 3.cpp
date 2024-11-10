#include <iostream>
using namespace std;

int main() {
    int x = 25;
    int y = x;
    int* z = &x;
    cout << "The value of x is " << x << endl;
    cout << "The address of memory for x is " << &x << endl;
    cout << "The value of y is " << y << endl;
    cout << "The address of memory for y is " << &y << endl;
    cout << "The value of z is " << z << endl;
    cout << "The address of memory for z is " << &z << endl;

    cout << "The value of *z=" << *z << endl;

    return 0;
}