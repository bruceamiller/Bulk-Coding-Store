#include <iostream>
#include <list>
#include <vector>

using namespace std;

class HashTable {
    private:
        vector<list<int>> table;
        int size;

        int hashFunction(int key) {
            return key % size;
        }

    public:
        HashTable(int s) : size(s) {
            table.resize(size);
        }

        void insert(int key) {
            int index = hashFunction(key);
            table[index].push_back(key);
        }

        void display() {
            for (int i = 0; i < size; ++i) {
                cout << i << ": ";
                for (int key : table[i])
                    cout << key << " -> ";
                cout << "NULL" << endl;
            }
        }
};

int main() {
    HashTable ht(7);
    ht.insert(10);
    ht.insert(20);
    ht.insert(15);
    ht.insert(7);
    
    ht.display();
    return 0;
}