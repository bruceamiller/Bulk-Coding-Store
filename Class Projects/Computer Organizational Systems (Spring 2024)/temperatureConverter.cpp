#include <iostream>
using namespace std;

int main() {
    float temperature;
    char unit;
    float newTemp;
    
    // TODO: Prompt user to enter temperature
    cout << "Enter temperature value: ";
    cin >> temperature;

    // TODO: Prompt user to enter unit (F for Fahrenheit, C for Celsius)
    cout << "Enter unit (F for Fahrenheit, C for Celsius): ";
    cin >> unit;
    
    // TODO: Convert temperature to the other unit
    if( unit == 'F' ) {
        // Convert Fahrenheit to Celsius
        // TODO: Implement the conversion formula here
        newTemp = (temperature - 32) *  5 / 9 ;
        cout << newTemp << " C";
    } else if( unit == 'C' ) {
        // Convert Celsius to Fahrenheit
        // TODO: Implement the conversion formula here
        newTemp = (temperature * 9 / 5) + 32;
        cout << newTemp << " F";
    } else {
        cout << "Invalid unit.";
        // Handle invalid input
        // TODO: Display an error message
    }

    return 0;
}

