#include <iostream>
#include <string>
#include <vector>
using namespace std;

//#define DEBUG

int main() {
    vector<pair<int,int>> bookshelf;
    string currentInput;
    int shelfSize;

    int bookID;
    int bookWidth;
    int booksOnShelf = 0;
    int problemNumber = 1;

    cin >> shelfSize;
    while (shelfSize != -1) {
        #ifdef DEBUG
            cout << "[";
            for (int i = 0; i < booksOnShelf; i++) {
                cout << "<" << bookshelf[i].first << ", " << bookshelf[i].second << ">,";
            }
            cout << "]" << endl;
        #endif
        cin >> currentInput;
        if (currentInput == "A") {
            cin >> bookID >> bookWidth;
            
            #ifdef DEBUG
            cout << bookID << " " << bookWidth;
            #endif
            
            //Add book to shelf
            bookshelf.insert(bookshelf.begin() + 0, pair(bookID, bookWidth));
            booksOnShelf++;
            
            //Check and remove books if they are off the edge.
            int totalWidth = 0;
            for (int i = 0; i < booksOnShelf; i++) {
                totalWidth += bookshelf[i].second;
                if (totalWidth > shelfSize) {
                    bookshelf.erase(bookshelf.begin() + i, bookshelf.end());
                    booksOnShelf = i;
                    break;
                }
            }
        } else if (currentInput == "R") {
            cin >> bookID;
            //Remove book
            for (int i = 0; i < booksOnShelf; i++) {
                if (bookshelf[i].first == bookID) {
                    bookshelf.erase(bookshelf.begin() + i);
                    booksOnShelf--;
                }
            }
        } else if (currentInput == "E") {
            cout << "PROBLEM " << problemNumber << ": ";
            for (int i = 0; i < booksOnShelf; i++) {
                cout << bookshelf[i].first << " ";
            }
            cout << endl;
            cin >> shelfSize;
            cout << endl;
            bookshelf.clear();
            booksOnShelf = 0;
        } else {
            break;
        }
    }



    //'E' means end of string
    return 0;
}