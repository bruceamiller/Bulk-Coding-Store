#include <iostream>
#include <bits/stdc++.h>
#include <string>
#include <vector>
using namespace std;

bool isNumber(char c);
int singleNumFromString(string s);
int stringMatchesInCurrentPosition(string AStr, int AStrPos, string BStr);

int main() {
    ifstream inputFile("AOC3.txt");
    string inputString;

    int total;
    bool enabledMuls = true;

    while (getline(inputFile, inputString)) {
        cout << "x";
        for (int i = 0; i < inputString.size(); i++) {
            string doInstruction = "do()";
            string dontInstruction = "don't()";

            if (stringMatchesInCurrentPosition(inputString, i, doInstruction)) {
                enabledMuls = true;
            }
            if (stringMatchesInCurrentPosition(inputString, i, dontInstruction)) {
                enabledMuls = false;;
            }
            
            if (enabledMuls and inputString[i] == 'm' and inputString[i+1] == 'u' and inputString[i+2] == 'l' and inputString[i+3] == '(') {
                string firstNumString = "";
                string secondNumString = "";
                int j = i+4;
                while (isNumber(inputString[j])) {
                    firstNumString += inputString[j];
                    j++;
                }
                if ((inputString[j] == ',') and firstNumString != "") {
                    j++;
                    while (isNumber(inputString[j])) {
                        secondNumString += inputString[j];
                        j++;
                    }
                    if (inputString[j] == ')' and secondNumString != "" and firstNumString.size() < 4 and secondNumString.size() < 4) {
                        //cout << "mul(" << firstNumString << "," << secondNumString << ")-";
                        total += (singleNumFromString(firstNumString) * singleNumFromString(secondNumString));
                    }
                }
            }
        }
    }
    cout << total;
    return 0;
}




bool isNumber(char c) {
    vector<char> nums = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'};

    if (count(nums.begin(), nums.end(), c)) {
        return true;
    }
    return false;
}

int singleNumFromString(string s) {
    istringstream numStream(s);
    int val;
    numStream >> val;
    return val;
}

int stringMatchesInCurrentPosition(string AStr, int AStrPos, string BStr) {
    for (int j = 0; j < BStr.size(); j++) {
        if (AStr[AStrPos + j] != BStr[j]) {
            return false;
        }
    }
    return true;
}