#include <iostream>
#include <string>
#include <set>

using namespace std;

int main() {
    set<string> setOfNumbers;

    setOfNumbers.insert("first");
    setOfNumbers.insert("second");
    setOfNumbers.insert("third");
    setOfNumbers.insert("first");

    cout << "Set size = " << setOfNumbers.size() << endl;

    for (set<string>::iterator it = setOfNumbers.begin(); it != setOfNumbers.end() ; ++it) {
        cout << *it << ' ';
    }
    cout << endl;

    set<string>::iterator it = setOfNumbers.find("second");
    if (it != setOfNumbers.end())
        cout << "'second' found" << endl;
    else
        cout << "'second' not found" << endl;
    
    return 0;
}