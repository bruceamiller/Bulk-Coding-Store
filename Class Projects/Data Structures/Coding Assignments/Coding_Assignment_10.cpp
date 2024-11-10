#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* next;
};

class SinglyLinkedList {
    private:
        Node* head;
        Node* tail;
        int listSize;
    public:
        SinglyLinkedList() : head(nullptr), tail(nullptr), listSize(0) {}

        bool empty() {
            return listSize ==0;
        }

        int size() {
            return listSize;
        }

        int front() {
            if (head != nullptr) {
                return head->data;
            }
            throw runtime_error("List is empty!");
        }

        int back() {
            if (tail != nullptr) {
                return tail->data;
            }
            throw runtime_error("List is empty!");
        }

        void push_front(int newData) {
            Node* newNode = new Node();
            newNode->data = newData;
            newNode->next = head;
            head = newNode;
            if (tail == nullptr) {
                tail = newNode;
            }
            listSize++;
        }

        void push_back(int newData) {
            Node* newNode = new Node();
            newNode->data = newData;
            newNode->next = nullptr;

            if (tail == nullptr) {
                head = newNode;
                tail = newNode;
            } else {
                tail->next = newNode;
                tail = newNode;
            }
            listSize++;
        }

        void pop_front() {
            if (head == nullptr) {
                throw runtime_error("Cannot pop from an empty list!");
            }
            
            Node* temp = head;
            head = head->next;
            delete temp;
            listSize--;

            if (head == nullptr) {
                tail == nullptr;
            }
        }

        void printList() {
            if (empty()) {
                cout << "List is empty." << endl;
                return;
            }
            Node* temp = head;
            while (temp != nullptr) {
                cout << temp->data << " -> ";
                temp = temp->next;
            }
            cout << "nullptr" << endl;
        }

        ~SinglyLinkedList() {
            while (head != nullptr) {
                Node* temp = head;
                head = head->next;
                delete temp;
            }
        }
};

int main() {
    SinglyLinkedList list;

    list.push_back(10);
    list.push_front(20);
    list.push_back(30);
    list.push_back(40);
    list.push_front(50);

    cout << "List after push operations: ";
    list.printList();

    cout << "Size of the list: " << list.size() << endl;
    cout << "Is the list empty? " << (list.empty() ? "Yes" : "No") << endl;
    
    cout << "Front of the list: " << list.front() << endl;
    cout << "Back of the lsit: " << list.back() << endl;

    list.pop_front();
    cout << "List after pop_front: ";
    list.printList();

    return 0;
}