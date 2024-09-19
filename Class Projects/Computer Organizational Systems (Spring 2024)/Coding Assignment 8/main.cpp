#include "rectangle.h"
#include <iostream>
using namespace std;

int main() {
    Rectangle rect1(5, 5);
    Rectangle rect2 = rect1;

    cout << "Area of rect1: " << rect1.area() << endl;
    cout << "Area of rect2: " << rect2.area() << endl;

    return 0;
}

