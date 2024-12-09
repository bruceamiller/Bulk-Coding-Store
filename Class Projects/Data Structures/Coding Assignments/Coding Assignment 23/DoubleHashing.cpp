#include <iostream>
#include <vector>

using namespace std;

class DoubleHashing {
    private:
        vector<int> table;
        int size;
        int hash1(int key) {
            return key % size;
        }
        int hash2(int key) {
            return 1 + (key % (size - 1));
        }

    public:
        DoubleHashing(int s) : size(s) {
            table.resize(size, -1);
        }

        void insert(int key) {
            int index = hash1(key);
            int step = hash2(key);

            while (table[index] != -1) {
                index = (index + step) % size;
            }
            table[index] = key;
        }
        
        void display() {
            for (int i = 0; i < size; ++i)
                cout << i << ": " << (table[i] == -1 ? "NULL" : to_string(table[i])) << endl;
        }
};

int main() {
    DoubleHashing dh(7);
    dh.insert(10);
    dh.insert(20);
    dh.insert(15);
    dh.insert(7);

    dh.display();
    return 0;
}