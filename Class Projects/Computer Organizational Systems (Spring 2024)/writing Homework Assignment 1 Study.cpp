#include<iostream>
using namespace std;


int main() {
    int xmain = 5;
    const int& x = xmain;
    
    xmain += 1;
    x += 1;

    cout << xmain;

}