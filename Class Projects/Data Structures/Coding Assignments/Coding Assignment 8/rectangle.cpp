#include "rectangle.h"
#include <iostream>
using namespace std;

Rectangle::Rectangle(int a, int b) : width(a), height(b) {};

Rectangle::Rectangle(const Rectangle &obj) {
    width = obj.width;
    height = obj.height;
    cout << "Copy constructor called." << endl;
};

Rectangle::~Rectangle() {
    cout << "Destructor called." << endl;
};

int Rectangle::area() {
    return width * height;
};