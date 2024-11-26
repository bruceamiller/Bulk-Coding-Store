#include <iostream>

using namespace std;


struct Node {
    Node* parent = nullptr;
    
    int data;

    Node* left;
    Node* right;

    Node(int value) : data(value), left(nullptr), right(nullptr) {}
};

class BinaryTree {
    public:
        Node* root;

        BinaryTree() : root(nullptr) {}

        void insertRoot(int value) {
            if (root == nullptr) {
                root = new Node(value);
            } else {
                cout << "Root already exists!" << endl;
            }
        }

        void insertLeft(Node* parent, int value) {
            if (parent->left == nullptr) {
                parent->left = new Node(value);
            } else {
                cout << "Left child already exists!" << endl;
            }
        }

        void insertRight(Node* parent, int value) {
            if (parent->right == nullptr) {
                parent->right = new Node(value);
            } else {
                cout << "Right child already exists!" << endl;
            }
        }

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
                inOrder(node->left);
            }
            if (node->right != nullptr) {
                inOrder(node->right);
            }
        }

        void postOrder(Node* node) {
            if (node->left != nullptr) {
                inOrder(node->left);
            }
            if (node->right != nullptr) {
                inOrder(node->right);
            }
            cout << node->data << " ";
        }

        // Binary Search tree functions:
        Node* insert(Node* node, int key) {
            if (node == nullptr) {
                return new Node(key);
            }

            if (key < node->data) {
                node->left = insert(node->left, key);
            } else if (key > node->data) {
                node->right = insert(node->right, key);
            }

            return node;
        }

        Node* search(Node* node, int key) {
            if (node == nullptr || node->data == key) {
                return node;
            }

            if (key > node->data) {
                return search(node->right, key);
            }

            return search(node->left, key);
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

        Node* minValueNode(Node* node) {
            Node* current = node;
            while (current && current->left != nullptr) {
                current = current->left;
            }
            return current;
        }
};

/*
int main() {
    BinaryTree tree;

    tree.insertRoot(1);

    tree.insertLeft(tree.root, 2);
    tree.insertRight(tree.root, 3);

    tree.insertLeft(tree.root->left, 4);
    tree.insertRight(tree.root->left, 5);

    cout << "In-order Traversal: ";
    tree.inOrder(tree.root);
    cout << endl;

    cout << "Pre-order Traversal: ";
    tree.preOrder(tree.root);
    cout << endl;

    cout << "Post-order Traversal: ";
    tree.postOrder(tree.root);
    cout << endl;

    return 0;
}
*/

int main () {
    BinaryTree bst;

    bst.root = bst.insert(bst.root, 8);
    bst.insert(bst.root, 3);
    bst.insert(bst.root, 10);
    bst.insert(bst.root, 1);
    bst.insert(bst.root, 6);
    bst.insert(bst.root, 4);
    bst.insert(bst.root, 7);
    bst.insert(bst.root, 14);
    bst.insert(bst.root, 13);

    Node* result = bst.search(bst.root, 6);
    if (result != nullptr) {
        cout << "Node found: " << result->data << endl;
    } else {
        cout << "Node not found" << endl;
    }

    cout << "In-order traversal before deletion: ";
    bst.inOrder(bst.root);
    cout << endl;

    bst.root = bst.deleteNode(bst.root, 3);
    
    cout << "In-order traversal after deletion 3: ";
    bst.inOrder(bst.root);
    cout << endl;
}