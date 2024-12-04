#include <iostream>
using namespace std;

const int HASH_MAP_SIZE = 100;

struct HashMapEntry {
    int* key =  nullptr;
    int* val = nullptr;
};

class HashMap {
    public:
        HashMapEntry EntryArray[HASH_MAP_SIZE];
        HashMap() {
            HashMapEntry EntryArray[HASH_MAP_SIZE];
        }

        int search(int key) {
            if (*EntryArray[key % HASH_MAP_SIZE].val != nullptr) {
                int val = *EntryArray[key % HASH_MAP_SIZE].val;
                return val;
            }
            return -1;
            cout << "Value not found";
        }
        
        int insert(int key, int value) {
            
        }
};


int main() {
    return 0;
}