#include <Iostream>
#include "SLinkedlist.h"

using namespace std;

int main() {
    SLinkedList<int> numlist;

    if (numlist.empty())
        cout << "You successfully made an empty list!" <<endl;

    numlist.addFront(2);
    cout << numlist.front() << endl;

    numlist.addFront(7);
    cout << numlist.front() << endl;

    numlist.removeFront();
    cout << numlist.front() << endl;

    SLinkedList<char> charlist;

    charlist.addFront('b');
    charlist.addFront('d');
    cout << charlist.front() << endl;

    charlist.removeFront();
    cout << charlist.front() << endl;
    
    return 0;
}
