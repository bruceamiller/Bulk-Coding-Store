#include <iostream>
using namespace std;

class TravelLog {
  public:
    /** initialize a new (empty) log.  */
    TravelLog() { }

    /** Add a new entry to the log.
     *  @param   speed      current speed in miles per hour
     *  @param   clockTime  elapsed time since beginning of trip (in hours)
     */
    void addEntry(int speed, int clockTime) {         
        totalMiles += speed * (clockTime - traveledTime);
        traveledTime = clockTime;
    }

    /** Returns the total number of miles traveled.
     *  @return number of miles
     */
    int getTotalMiles() const { return totalMiles; }

  private:
    int traveledTime = 0;
    int totalMiles = 0;
    //  ??? state information ???

};

int main() {
    int inputNum, speed, clockTime;
    bool onMph = true, getNewLog = true;
    cin >> inputNum;
    while(getNewLog) {
        TravelLog currentLog;
        while (inputNum >= 10) {
            speed = inputNum;
            cin >> clockTime;
            cin >> inputNum;
            currentLog.addEntry(speed, clockTime);
        }
        cout << currentLog.getTotalMiles() << "miles" << endl;
        if (inputNum == -1) { getNewLog = false; }
        cin >> inputNum;
    }
}

