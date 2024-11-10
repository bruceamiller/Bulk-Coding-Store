#include <iostream>

using namespace std;

class Queue {
    private:
        int* arr;
        int capacity;
        int frontIndex;
        int backIndex;
        int count;
    public:
        Queue(int size = 10) {
            arr = new int[size];
            capacity = size;
            frontIndex = 0;
            backIndex = -1;
            count = 0;
        }

        ~Queue() { delete[] arr; }

        void push(int val) {
            if (size() == capacity) {
                cout << "Queue is full" << endl;
                return;
            }
            backIndex = (backIndex + 1) % capacity;
            arr[backIndex] = val;
            count++;
        }

        void pop() {
            if (empty()) {
                cout << "Queue is empty" << endl;
                return;
            }
            frontIndex = (frontIndex + 1) % capacity;
            count--;
        }

        int front() {
            if (!empty()) {
                return arr[frontIndex];
            } else {
                cout << "Queue is empty" << endl;
                return -1;
            }
        }

        int back() {
            if (!empty()) {
                return arr[backIndex];
            } else {
                cout << "Queue is empty" << endl;
                return -1;
            }
        }



        int size() { return count;}

        bool empty() {
            return (count == 0);
        }
};

int main() {
    Queue q(5);
    q.push(10);
    q.push(20);
    q.push(30);
    cout << "Front: " << q.front() << endl;
    cout << "Back: " << q.back() << endl;
    q.pop();
    cout << "Front: " << q.front() << endl;
    q.push(40);
    q.push(50);
    q.push(60);
    q.push(70);
    q.push(8);
    return 0;
}