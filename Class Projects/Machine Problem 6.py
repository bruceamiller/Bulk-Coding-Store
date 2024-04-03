from MP6_StudentClass import Student

#
# Machine Problem 5
# CS 1300
# Bruce Miller
#
# Description:
#
# Get studentd ID, name, testScores, and testAvg
# Print everything in organized & labeled lines
#

def getStudents():
    #
    # Opens the data file of student info... studentID, firstName, lastName, then
    # testScores - the number of test scores is variable, from zero up... reads
    # each line of data as a str, divides the line into the values... str, str, str,
    # int, int, int... (a variable number of int values - could be none)...
    # instantiates a new Student object, uses the Student object's instance methods
    # to add those values to the object, adds the Student object to a list of objects,
    # and returns the list of Student objects.
    #
    # There are no parameters.
    #
    # Returns a list of objects from the Student class
    #

    file = open("C:\\Users\\Bruce\\Desktop\\Python Coding\\Class Projects\\1300 - MP6 Data.txt")
    lines = file.readlines()
    file.close()
    for linePos in range(len(lines)):
        lines[linePos] = lines[linePos].split()

    roster = []
    for studentInfo in lines:
        currentStudent = Student(studentInfo[0])
        currentStudent.setName(studentInfo[1], studentInfo[2])
        for testScore in studentInfo[3:]:
            currentStudent.addTest(int(testScore))
        roster.append(currentStudent)
    
    return roster

def printStudents(roster):
    #
    # Prints the information for each Student object in roster... including studentID,
    # firstName, lastName, testScores, and average for each object.
    #
    # roster A list of objects from the Student class, each object contains a
    # studentID(str), firstName(str), lastName(str),
    # testScores(list of int value), and average (float).
    #
    # There is no return value.
    #

    print("Students in roster:")
    for student in roster:
        print()
        name = student.getName()
        scoresText = ""
        for score in student.getTestScores():
            scoresText += str(score) + " "
        print("Student:", student.getID(), name[0], name[1])
        print("Test Scores:", scoresText)
        print(f"Test Average: {student.getAvg():.2f}")


roster = getStudents()

printStudents(roster)