#include <iostream>
#include <string>

using namespace std;


bool isPrefix(string a, string b) {
    if (a.size() > b.size()) return false;
    return b.substr(0, a.size()) == a;
}


int main() {
    // Get list of strings
    string stringList[40];
    int currentStringPos = 0;
    cin >> stringList[currentStringPos];


    //End string list by inputting forty number strings, or inputting invalid number "-1"
    while (currentStringPos < 40 and stringList[currentStringPos] != "-1") {
        currentStringPos++;
        cin >> stringList[currentStringPos];
        cout << "\"" << stringList[currentStringPos] << "\"" << endl;
    }

    //Brute force compare all strings
    for (int i = 0; i < currentStringPos + 1; i++) {
        for (int j = 0; j < currentStringPos + 1; j++) {
            if(i != j and isPrefix(stringList[i], stringList[j])) {
                cout << "No" << endl;
                return 0;
            }
        }
    }
    cout << "Yes" << endl;
    return 0;
}