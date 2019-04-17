#testing
def initialize():
    global textLength
    textLength=0

def getTextLength():
    return textLength

def setTextLength(text):
    textLength = len(text)

#password is easy, its the length of the text + 
#the row jump timer, which is just a random int between 10-100
def generatePassword(text):
    length=len(text)
    length = str(length)
    #needs to check if image has enough pixels per row to accomodate int
    #for now, keeping it hardcoded
    #rjt = random.randint(10,99)
    rjt=10
    rjt=str(rjt)
    return (length+rjt)
    

