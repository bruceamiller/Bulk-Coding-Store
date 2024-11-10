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

    public:
        SinglyLinkedList() {
            head = nullptr;
            tail = nullptr;
            cout << "head and tail nodes are initiated with nullpoint" << endl;
        }

        void push_back(int elem) {
            Node* newNode = new Node;
            newNode->data = elem;
            newNode->next = nullptr;

            if (head == nullptr) {
                head = newNode;
                tail = newNode;
            }
            else {
                tail->next = newNode;
                tail = newNode;
            }
        }
        
        void push_front (int elem) {
            Node* newNode = new Node;
            newNode->data = elem;
            newNode->next = nullptr;

            if (head == nullptr) {
                head = newNode;
                tail = newNode;
            } else {
                newNode->next = head;
                head = newNode;
            }
        }

        void printList() {
            Node *tmp;
            tmp = head;
            while (tmp != nullptr) {
                cout << tmp->data << " ";
                tmp = tmp -> next;
            }
            cout << endl;
        }
};



int main() {
    SinglyLinkedList numList1;

    numList1.push_back(30);
    numList1.push_back(40);
    numList1.push_front(20);
    numList1.push_front(10);
    numList1.printList();

    return 0;
}