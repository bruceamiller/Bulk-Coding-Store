#include<iostream>
using namespace std;

template <typename T>
void myswap (T& x, T& y) {
    T temp = x;
    x = y;
    y = temp;
    return;
}

int main() {
    int a = 100, b = 200;
    cout << "Before swap: " << a << ", " << b << endl;
    myswap(a, b);
    cout << "After swap: " << a << ", " << b << endl;

    double c = 23.5, d = 55.8;
    cout << "Before swap: " << c << ", " << d << endl;
    myswap(c, d);
    cout << "After swap: " << c << ", " << d << endl;
    return 0;
}