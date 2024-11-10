#include <iostream>
using namespace std;

//function definition to swap the values.
void mySwap(int* x, int* y) {
    cout << "-- Before swap function, *x=" << *x << ", y=" << *y << endl;
    int temp;
    temp = *x;
    *x = *y;
    *y = temp;
    cout << "-- After swap function, *x=" << *x << ", y=" << *y << endl;
}

int main() {
    int a = 100, b = 200;

    cout << "Before swap, a=" << a << ", b=" << b << endl;
    mySwap(&a, &b);
    cout << "after swap, a=" << a << ", b=" << b << endl;

    return 0;
}
