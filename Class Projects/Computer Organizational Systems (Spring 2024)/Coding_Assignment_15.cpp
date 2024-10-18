#include <iostream>
#include <stack>
using namespace std;

template<typename T>
void reverseArray(T arr[], int n) {
    stack<T> stack;

    for (int i = 0; i < n; i++) {
        stack.push(arr[i]);
    }

    for (int i = 0; i < n; i++) {
        arr[i] = stack.top();
        stack.pop();
    }
    
}

int main() {
    int arr[] = {1, 2l, 3, 4, 5};

    int n = 5;

    reverseArray(arr, n);

    for (int i = 0; i < n; ++i)
        cout << arr[i] << " ";
}