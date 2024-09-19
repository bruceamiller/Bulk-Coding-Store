import math

def rotateAroundCenter(objectPos, centerPos, angle):
    vectorFromCenter = [0.0, 0.0]
    for i in range(2):
        vectorFromCenter[i] = centerPos[i] - objectPos[i]
    rotatedVector = [0.0, 0.0]
    rotatedVector[0] = vectorFromCenter[0] * math.cos(angle) - vectorFromCenter[1] * math.sin(angle)
    rotatedVector[1] = vectorFromCenter[0] * math.sin(angle) + vectorFromCenter[1] * math.cos(angle)
    for i in range(2):
        objectPos[i] += rotatedVector[i] - vectorFromCenter[i]
    return objectPos[i]

def newLengthVector(oldVector, length):
    ratio = length / math.hypot(oldVector[0], oldVector[1])
    newVector = []
    for i in range(len(oldVector)):
        newVector.append(oldVector[i] * ratio)
    return newVector
