#include <iostream>
using namespace std;

struct node {
    int data;
    node* next;
};

class SLinkedList {
    private:
        node* head;
        node* tail;

    public:
        SLinkedList() {
            head = nullptr;
            tail = nullptr;
            cout << "head and tail nodes are initiated with nullpoint" << endl;
        }

        void ListAppend(int elem) {
            node* newNode = new node;
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
        
        void ListPrepend (int elem) {
            node* newNode = new node;
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

        void InsertAfter(node* curNode, int elem) {
            node* newNode = new node;
            newNode->data = elem;
            newNode->next = nullptr;
            
            if (head == nullptr) {
                head = newNode;
                tail = newNode;
            } else if (curNode == tail) {
                tail->next = newNode;
                tail = newNode;
            } else {
                newNode->next = curNode->next;
                curNode->next = newNode;
            }
        }

        void RemoveAfter(node* curNode) {
            if (head == nullptr) {
                cout << "List is empty. Nothing to remove." << endl;
                return;
            }

            if (curNode == nullptr && head != nullptr) {
                node* sucNode = head->next;
                delete head;
                head = sucNode;

                if (head == nullptr) {
                    tail = nullptr;
                }
                return;
            }
            if (curNode->next != nullptr) {
                node* sucNode = curNode->next;
                curNode->next = sucNode->next;
                if (sucNode == tail) {
                    tail = curNode;
                }

                delete sucNode;
            }
        }

        void ListDisplay() {
            node *tmp;
            tmp = head;
            while (tmp != nullptr) {
                cout << tmp->data << " ";
                tmp = tmp -> next;
            }
            cout << endl;
        }

        node* getNode(int value) {
            node* tmp = head;
            while (tmp != nullptr) {
                if (tmp->data == value) {
                    return tmp;
                }
                tmp = tmp->next;
            }
            return nullptr;
        }

        node* Search(int value) {
            //GetNode function from notes acts the same as the search function, so I just copied it.
            //You start at the head. If the head is empty, then the list is empty, and no value can be contained within, so you just return nullptr;
            //You go through each value in the list, until you reach the end node "nullptr"
            //If you find a value you, return the value position stored in your current postion "tmp" and are done.
            //If you don't find the value you return nullptr, because it wasn't found int the list.
            node* tmp = head;
            while (tmp != nullptr) {
                if (tmp->data == value) {
                    return tmp;
                }
                tmp = tmp->next;
            }
            return nullptr;
        }
};

void printFoundSearch(node* currentNode, int value) {
    //If it returns nullptr, then you didn't find the value...
    //Had to include the value in the function input, so that it could be printed, whether or not it was contained within the given node.
    if (currentNode == nullptr) {
        cout << "Value " << value << " not found in the list" << endl;
    } else {
        cout << "Node with value " << value << " found." << endl;
    }
}

int main() {
    SLinkedList numList;
    node* unused;

    printFoundSearch(numList.Search(-99), -99);

    numList.ListAppend(20);
    numList.ListPrepend(10);
    numList.ListAppend(30);
    numList.ListAppend(40);
    numList.ListDisplay();

    numList.ListPrepend(5);
    numList.ListPrepend(1);
    numList.ListDisplay();

    numList.InsertAfter(numList.getNode(20), 25);
    numList.ListDisplay();

    numList.RemoveAfter(numList.getNode(10));
    numList.ListDisplay();

    printFoundSearch(numList.Search(30), 30);
    printFoundSearch(numList.Search(50), 50);

    
}
