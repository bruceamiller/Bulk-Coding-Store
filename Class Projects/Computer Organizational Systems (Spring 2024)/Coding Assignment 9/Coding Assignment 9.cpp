#include <iostream>
#include <stdexcept>

using namespace std;

int main() {
    try {
        throw runtime_error("An error occurred");
    } catch (const exception& e) {
        cout << e.what() << endl;
    }

    return 0;
}
