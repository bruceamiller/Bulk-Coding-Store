#include <iostream>

using namespace std;


struct Node {
    Node* parent = nullptr;
    
    int data;

    Node* left;
    Node* right;

    int height;

    Node(int value) : data(value), left(nullptr), right(nullptr), height(1) {}
};

class AVLTree {
    public:
        Node* root;

        AVLTree() : root(nullptr) {}

        //Insertion and deletion

        void insertRoot(int value) {
            if (root == nullptr) {
                root = new Node(value);
            } else {
                cout << "Root already exists!" << endl;
            }
        }

        Node* insert(Node* node, int key) {
            if (node == nullptr) {
                return new Node(key);
            }

            if (key < node->data) {
                node->left = insert(node->left, key);
            } else if (key > node->data) {
                node->right = insert(node->right, key);
            } else {
                return node;
            }

            int leftHeight = 0, rightHeight = 0;
            if (node->left) {
                leftHeight = node->left->height;
            }if (node->right) {
                rightHeight = node->right->height;
            }
            node->height = 1 + max(leftHeight, rightHeight);

            int balanceFactor = leftHeight - rightHeight;

            if (balanceFactor > 1 && key < node->left->data) {
                return rotateRight(node);
            }

            if (balanceFactor < -1 && key > node->right->data) {
                return rotateLeft(node);
            }

            if (balanceFactor > 1 && key > node->left->data) {
                node->left = rotateLeft(node->left);
                return rotateRight(node);
            }

            if (balanceFactor < -1 && key < node->right->data) {
                node->right = rotateRight(node->right);
                return rotateLeft(node);
            }

            return node;
        }

        Node* deleteNode(Node* root, int key) {
            if (root == nullptr) return root;

            if (key < root->data) {
                root->left = deleteNode(root->left, key);
            } else if (key > root->data) {
                root->right = deleteNode(root->right, key);
            } else {
                if (root->left == nullptr) {
                    Node* temp = root->right;
                    delete root;
                    return temp;
                } else if (root->right == nullptr) {
                    Node* temp = root->left;
                    delete root;
                    return temp;
                }

                Node* temp = minValueNode(root->right);

                root->data = temp->data;

                root->right = deleteNode(root->right, temp->data);
            }
            return root;
        }

        //AVL rotation functions:

        Node* rotateRight(Node* y) {
            Node* x = y->left;
            Node* T2 = x->right;

            x->right  =y;
            y->left = T2;

            int leftHeight = 0, rightHeight = 0;
            if (y->left) {
                leftHeight = y->left->height;
            }
            if (y->right) {
                rightHeight = y->right->height;
            }
            y->height = 1 + max(leftHeight, rightHeight);

            leftHeight = 0, rightHeight = 0;
            if (x->left) {
                leftHeight = x->left->height;
            }
            if (x->right) {
                rightHeight = x->right->height;
            }
            x->height = 1 + max(leftHeight, rightHeight);

            return x;
        }

        Node* rotateLeft(Node* x) {
            Node* y = x->right;
            Node* T2 = y->left;

            y->left = x;
            x->right = T2;

            int leftHeight = 0, rightHeight = 0;

            if (x->left) {
                leftHeight = x->left->height;
            }
            if (x->right) {
                rightHeight = x->right->height;
            }
            if (x->right) {
                rightHeight = x->left->height;
            }
            x->height = 1 + max(leftHeight, rightHeight);

            leftHeight = 0, rightHeight = 0;
            if (y->left) {
                leftHeight = y->left->height;
            }
            if (y->right) {
                rightHeight = y->right->height;
            }
            y->height = 1 + max(leftHeight, rightHeight);

            return y;
        }


        //Tree Searching Functions

        Node* search(Node* node, int key) {
            if (node == nullptr || node->data == key) {
                return node;
            }

            if (key > node->data) {
                return search(node->right, key);
            }

            return search(node->left, key);
        }

        Node* minValueNode(Node* node) {
            Node* current = node;
            while (current && current->left != nullptr) {
                current = current->left;
            }
            return current;
        }

        //Tree reading functions

        void inOrder(Node* node) {
            if (node->left != nullptr) {
                inOrder(node->left);
            }
            cout << node->data << " ";
            if (node->right != nullptr) {
                inOrder(node->right);
            }
        }

        void preOrder(Node* node) {
            cout << node->data << " ";
            if (node->left != nullptr) {
                preOrder(node->left);
            }
            if (node->right != nullptr) {
                preOrder(node->right);
            }
        }

        void postOrder(Node* node) {
            if (node->left != nullptr) {
                postOrder(node->left);
            }
            if (node->right != nullptr) {
                postOrder(node->right);
            }
            cout << node->data << " ";
        }
};


void printTraversals(AVLTree avl) {
    cout << "In-order traversal: ";
    avl.inOrder(avl.root);
    cout << endl;

    cout << "Pre-order traversal: ";
    avl.preOrder(avl.root);
    cout << endl;
}

int main () {
    AVLTree avl;

    avl.root = avl.insert(avl.root, 33);
    avl.root = avl.insert(avl.root, 13);
    avl.root = avl.insert(avl.root, 53);
    avl.root = avl.insert(avl.root, 11);
    avl.root = avl.insert(avl.root, 21);
    avl.root = avl.insert(avl.root, 61);
    avl.root = avl.insert(avl.root, 8);

    cout << "In-order traversals after intitial insertions: ";
    avl.inOrder(avl.root);
    cout << endl;
    cout << "Pre-order traversal after initial insertions: ";
    avl. preOrder(avl.root);
    cout << endl;

    avl.root = avl.insert(avl.root, 9);

    cout << "In-order traversal after inserting 9: ";
    avl.inOrder(avl.root);
    cout << endl;

    cout << "Pre-order traversal after inserting 9: ";
    avl.preOrder(avl.root);
    cout << endl;

    avl.root = avl.deleteNode(avl.root, 13);

    cout << "In-order traversal after deleting 13: ";
    avl.inOrder(avl.root);
    cout << endl;

    cout << "Pre-order traversal after deleting 13: ";
    avl.preOrder(avl.root);
    cout << endl;

    int searchKey = 11;
    Node* searchResult = avl.search(avl.root, searchKey);
    if (searchResult) {
        cout << "Key" << searchKey << " found in the tree." << endl;
    } else {
        cout << "Key " << searchKey << " not found in the tree." << endl;
    }
    
    return 0;
}

//Here's the comparison between results: