#include <iostream>

#define DEBUG

using namespace std;

class Rectangle {
    public:
        Rectangle( int a = 1, int b = 2): width(a), height(b) {}

        ~Rectangle() {
            cout << "Destructor called" << endl;
        }

        int area() {
            return width * height;
        }
    
    private:
        int width;
        int height;
};

int main() {
    Rectangle rect1(5, 5);
    cout << "Area of rect1: " << rect1.area() << endl;

    Rectangle* rect2 = new Rectangle(3, 4);
    cout << "Area of rect2 (using arrow operator): " << rect2 -> area() << endl;

    delete rect2;

    return 0;
}
