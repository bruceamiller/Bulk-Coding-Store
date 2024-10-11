#include <iostream>
using namespace std;

class MyClass {
    private:
        int value;
    public:
        MyClass(int value) {
            this->value = value;
        }
        
        void display() {
            cout << "Value: " << this->value << endl;
        }

        MyClass& setValue(int value) {
            this->value = value;
            
            return *this;
        }
};



int main () {
    MyClass test(1);
    test.display();

    test.setValue(2);
    test.display();
    return 0;
}