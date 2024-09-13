#include <iostream>
using namespace std;

int getMaxPercentage(float imageDimension, float paperDimension) {
    int maxPercentage = imageDimension / paperDimension * 100;
    if (maxPercentage > 100) {
        maxPercentage = 100;
    }
    return maxPercentage;
}

int main() {
    float A, B, C, D;
    int ACPercentage, BDPercentage, rotBCPercentage, rotADPercentage;
    int percentage, rotPercentage;

    bool continueLoop = true;
    while (continueLoop) {
        continueLoop = false;
        cin >> A >> B >> C >> D;
        if (A && B && C && D) {
            continueLoop = true;
        }
        ACPercentage = getMaxPercentage(C, A);
        BDPercentage = getMaxPercentage(D, B);
        rotBCPercentage = getMaxPercentage(C, B);
        rotADPercentage = getMaxPercentage(D, A);
        if (ACPercentage < BDPercentage) {
            percentage = ACPercentage;
        } else {
            percentage = BDPercentage;
        }

        if (rotBCPercentage < rotADPercentage) {
            rotPercentage = rotBCPercentage;
        } else {
            rotPercentage = rotADPercentage;
        }
        
        if (rotPercentage > percentage) {
            percentage = rotPercentage;
        }
        if (A != 0 && B != 0 && C != 0 && D != 0) {
            cout << percentage << "%" << endl;
        }
    }
    return 0;
}