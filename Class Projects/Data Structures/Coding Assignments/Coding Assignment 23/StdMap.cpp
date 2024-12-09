#include <iostream>
#include <string>
#include <map>
#include <stdexcept>

using namespace std;

int main() {
    map<int, string> fruitMap;

    fruitMap[101] = "Apple";
    fruitMap[102] = "Banana";
    fruitMap[103] = "Cherry";

    cout << "Initial fruitMap content:\n";
    for (const auto& pair : fruitMap) {
        cout << pair.first << " => " << pair.second << endl;
    }
    cout << endl;

    fruitMap[104] = "Date";
    fruitMap[101] = "Apricot";

    try {
        cout << "Using at(): The fruit wiht key 102 is " << fruitMap.at(102) << endl;
    
        cout << "Using at() : The fruit with key 105 is " << fruitMap.at(105) << endl;
    } catch (const out_of_range& e) {
        cerr << "Error: " << e.what() << " (key 105 does not exist in the map)\n";
    }

    int searchKey = 103;
    auto it = fruitMap.find(searchKey);
    if (it != fruitMap.end()) {
        cout << "\nUsing find(): The fruit with key " << searchKey << " is " << it->second << endl;
    } else {
        cout << "\nUsing find(): Key " << searchKey << " not found in the map.\n";
    }

    cout << "\nFinal fruitMpa content:\n";
    for (const auto& pair : fruitMap) {
        cout << pair.first << " => " << pair.second << endl;
    }

    return 0;
}