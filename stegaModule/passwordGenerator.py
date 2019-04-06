#methods to analyze text length and space between pixels to determine
#password, and how to dissect it for length and pixel sequence
#need to connect this module to the encrpytion and decryption

#need to connnect this module
import random
def getPixelBufferNum(pw): #pw=password

    pw=str(pw)
    length=len(str(pw))
    pixelBuffer=int(pw[length-1]) # for simplciity sake, return int
    return pixelBuffer

def getTextLength(pw):
    pw=str(pw)
    return int(pw[0:-2])
######################

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
    

