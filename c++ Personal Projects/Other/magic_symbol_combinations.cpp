#include <iostream>
#include <set>
#include <string>

using namespace std;

int main() {
    int rowLength = 10;
    int currentRowPos = 0;

    set<string> symbolPairs ={"..", "oo", "o.", "o●", "||", "●|", "●.", "|.", "o|", "●●", ".8", "o8", "8●", "|8", "88", "●>", "8>", ".S", "|S", ">|", ".N", "oN",
    ">o", "8S", ".>", ".F", ".⫯", "So", "|⫯", "⫯N", "FN", "F|", "F>", "Fo", ".W", "8F", ".N", "o⫯", "|N", "S⫯", "oW", "●S", "8⫯", "8N", "●N", "SW", "SN", "●F", "●⫯",
    "⫯W", "F⫯", "FW", "SF", "NW", ">W", ">S", ">⫯", "8W", ">N", "|W", "●W"};
    string symbolList[] =
    {".",
    "o",
    "●",
    "|", "8",
    ">", "S", "F", "⫯", "N", "W"};
    string symbolNameList[] = {"SPOT", "HOLE", "LOOP", "FLOW", "CHAIN", "SHOOT", "WAVE", "FIX", "SLICE", "NET", "WEAVE"};

    bool viewSymbolNames = true;
    
    int listSize = size(symbolList);

    for (int i = 0; i < listSize; i++){
        for (int j = i; j < listSize; j++){
            if (symbolList[i] != symbolList[j] and !(symbolPairs.find(symbolList[i] + symbolList[j]) != symbolPairs.end()) and !(symbolPairs.find(symbolList[j] + symbolList[i]) != symbolPairs.end())){
                cout << symbolList[i] << symbolList[j] << " ";
                if (viewSymbolNames) {
                    cout << symbolNameList[i] << "-" << symbolNameList[j] << endl;;
                } else {
                    //Row Spacing

                    currentRowPos++;
                    if (currentRowPos == rowLength) {
                        cout << endl;
                        currentRowPos = 0;
                    }
                }
            }

        }   
    }



    return 0;
}