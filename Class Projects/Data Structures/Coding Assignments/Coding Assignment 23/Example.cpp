#include <iostream>
#include <map>
#include <unordered_map>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    map<string, int> wordMap = {
        {"is", 6},
        {"the", 5},
        {"hat", 9},
        {"at", 6}
    };

    cout << "std::map Contents : Elements are stored in sorted order of Keys (Balanced BST)\n";
    for_each(wordMap.begin(), wordMap.end(), [](pair<string, int> elem){
        cout << elem.first << " : " << elem.second << endl;
    });
    cout << endl;

    unordered_map<string, int> wordUOMap = {
        {"is", 6},
        {"the", 5},
        {"hat", 9},
        {"at", 6}
    };

    cout << "std::undordered_map Contents : Elements are stored in arbitrary order (Hash Table)\n";
    for_each(wordUOMap.begin(), wordUOMap.end(), [](pair<string,int> elem) {
        cout << elem.first << " : " << elem.second << endl;
    });

    return 0;
}