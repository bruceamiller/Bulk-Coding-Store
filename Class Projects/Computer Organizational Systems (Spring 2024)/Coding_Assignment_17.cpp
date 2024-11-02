#include <iostream>
using namespace std;

struct node {
    int data;
    node* next;
    node* prev;
};

class Deque {
    private:
        node* head;
        node* tail;
        int currentSize;
    
    public:
        Deque() {
            head = nullptr;
            tail = nullptr;
            currentSize = 0;
        }

        void push_front(int e) {
            node* newNode = new node;
            newNode->data = e;
            newNode->prev = nullptr;
            newNode->next = head;

            if (head == nullptr) {
                head = newNode;
                tail = newNode;
            } else {
                head->prev = newNode;
                head = newNode;
            }

            currentSize++;
        }

        void push_back(int e) {
            node* newNode = new node;
            newNode->data = e;
            newNode->next = nullptr;
            newNode->prev = tail;

            if (tail == nullptr) {
                head = newNode;
                tail = newNode;
            } else {
                tail->next = newNode;
                tail = newNode;
            }

            currentSize++;
        }

        void pop_front() {
            if (head == nullptr) {
                cout << "Deque Underflow" << endl;
                return;
            }

            node* temp = head;
            head = head->next;

            if (head != nullptr) {
                head->prev = nullptr;
            } else {
                tail = nullptr;
            }

            delete temp;
            currentSize--;
        }

        void pop_back() {
            if (tail == nullptr) {
                cout << "Deque Underflow" << endl;
                return;
            }

            node* temp = tail;
            tail = tail->prev;

            if (tail != nullptr) {
                tail->next = nullptr;
            } else {
                head = nullptr;
            }

            delete temp;
            currentSize--;
        }

        int front() {
            if (head == nullptr) {
                cout << "Deque is Empty" << endl;
                return -1;
            }

            return head->data;
        }

        int back() {
            if (tail == nullptr) {
                cout << "Deque is Empty" << endl;
                return -1;
            }

            return tail->data;
        }

        int size() {
            return currentSize;
        }

        bool empty() {
            return currentSize == 0;
        }

        ~Deque() {
            while (head != nullptr) {
                pop_front();
            }
        }
};

int main() {
    Deque dq;

    dq.push_back(10);
    dq.push_front(5);
    dq.push_back(15);
    dq.push_front(2);

    cout << "Front element: " << dq.front() << endl;
    cout << "Back element: " << dq.back() << endl;

    dq.pop_front();
    dq.pop_back();

    cout << "Front element after pop: " << dq.front() << endl;
    cout << "Back element after pop: " << dq.back() << endl;

    cout << "Size of deque: " << dq.size() << endl;

    cout << "Deque is " << (dq.empty() ? "empty" : "not empty") << endl;

    return 0;
}