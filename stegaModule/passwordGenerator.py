#methods to analyze text length and space between pixels to determine
#password, and how to dissect it for length and pixel sequence
def getRowHopNum(pw): #pw=password

    pw=str(pw)
    length=len(str(pw))
    rowHopNum=int(pw[length-2]+pw[length-1]) # for simplciity sake, return int
    return rowHopNum

def getTextLength(pw):
    pw=str(pw)
    return int(pw[0:-2])
######################

password=15310
print("Password:",password)
print("For this case, the row jumper is the last two digits, which is",getRowHopNum(password))
print("The text length is",getTextLength(password),"characters")    
