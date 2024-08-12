class Date():

    def __init__(self, month, day, year = None):
        self._year = int(year)
        self._month = int(month)
        self._day = int(day)

class Manwha():

    def __init__(self):
        self._Name = ""
        self._Current_Ch = ""
        self._Comment = ""
        self._Last_Read = ""
        self._Status = ""
        self._Tags = ""
    
    def setName(self, name):
        self._Name = name
    def setCurrentCh(self, current_ch):
        self._Current_Ch = current_ch
    def setComment(self, comment):
        self._Comment = comment
    def setLastRead(self, lastRead):
        self._Last_Read = lastRead
    def setStatus(self, status):
        self._Status = status
    def setTags(self, tags):
        self._Tags = tags
    
    def addTag(self, tag):
        self._Tags += " / " + tag
    
    def getName(self):
        return self._Name
    def getCurrentCh(self):
        return self._Current_Ch
    def getComment(self):
        return self._Comment
    def getLastRead(self):
        return self._Last_Read
    def getStatus(self):
        return self._Status
    def getTags(self):
        return self._Tags
    
    def __str__(self):
        return f"""Name: {self._Name}
Current Ch: {self._Current_Ch}
Comment: {self._Comment}
Last Read: {self._Last_Read}
Status: {self._Status}
Tags: {self._Tags}"""