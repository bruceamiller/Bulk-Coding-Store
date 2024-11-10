#ifndef SLINKEDLIST_H
#define SLINKEDLIST_H

#include <iostream>
#include <stdexcept>

using namespace std;

template <typename Object>
class SLinkedList {
    public:
        SLinkedList();
        ~SLinkedList();
        bool empty() const;
        const Object& front() const;
        void addFront(const Object& e);
        void removeFront();
    
    private:
        struct SNode {
            Object elem;
            SNode* next;
        };

        SNode* head;
};

#include "SLinkedList.tcc"
#endif