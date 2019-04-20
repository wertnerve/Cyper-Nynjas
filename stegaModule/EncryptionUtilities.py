import math
import random
#
# retrieveText takes in the decyrpted string of garbage and text and pulls the original message out using the flags
# This function also accounts for the start and end flags being the same.
def retrieveText(totalText):
    startFlag = totalText.find(getMessageFlag(1))  # finds the start of the opening flag
    print(startFlag)
    startFlag = startFlag + len(getMessageFlag(1))  # finds the end of the opening flag
    print(startFlag)
    endFlag = totalText.find(getMessageFlag(2), startFlag)  # finds the start of the closing flag
    print(endFlag)
    text = totalText[startFlag: endFlag]
    return text

# generates a string of random characters, at the moment ignoring '(' and ')', though that can be removed if we lengthen the flags
def garbageGen(x):
    garb = ""
    for i in range(x):
        char = chr(random.randint(32, 127))
        while (char == getMessageFlag(1) or char == getMessageFlag(2)):
            char = chr(random.randint(32, 127))
        garb = garb + char

    return garb

# defines the message flags, the starting flag is 1, and the ending flag is 2
def getMessageFlag(x):
    if x == 1:
       return 'KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK'
    if x == 2:
        return 'KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK'

# adds the flags to the beginning and the end of the message
# superceded by concatGarbageAndFlags
def concatMessageFlags(text):

    return getMessageFlag(1)+text+getMessageFlag(2)

# adds a random length of the garbage string, then the start flag, to the text, then adds the end flag and the remaining string of
# garbage to the end of the text
def concatGarbageAndFlags(text, garbage):
    splitzone = random.randint(0, len(garbage)-1)
    before = garbage[:splitzone]
    after = garbage[splitzone:]
    return before + getMessageFlag(1) + text + getMessageFlag(2) + after

# takes in file path for oriignal image, trims off the name of the image so encrypted image can eb saved in same directory
def trimFilename(text):
    x = len(text)-1
    char = text[x]
    while char is not '/':
        text=text[:-1]
        x = len(text)-1
        char = text[x]
    return text

# placeholder method for converting string of vignere characters into list
def convertToIntegerList(x):
    y = []
    i = 0
    for char in x:
        y.append(int(x[i]))
        print(y)
        i += 1
    return y

# Performs the euclidean algorithm to determine the gcd of two integers
# can be removed if not being used
def euclid_alg(a, b):
    r = 1
    while r is not 0:
        q = math.floor(a / b)
        r = a - b * q
        if r is 0:
            break
        a = b
        b = r
    return b

# performs modular exponentiation
# can be removed if not being used
def mod_exp(y, x, n):
    w, s, r = 0, 1, 1
    binary = bin(x)
    w = len(binary) - 2
    if w is 0 and x is 1:
        r = y % n
    elif w is not 0 or x is not 0:
        k = 0
        while k is not w:
            b = binary[k]
            if b is 1:
                r = s * y % n
            else:
                r = s
            s = r ** 2 % n
            k = k + 1
    return r

# Performs the Chinese Remainder Theorem
# can be removed if not being used
def chin_rem_them(a, m, b, n):
    if euclid_alg(m, n) is not 1:
        print("Error, m and n are not coprime. Ending Program")
        exit(0)
    mn = m * n
    i = mod_inverse(n, m)
    # k=(a-b)*i (mod m)
    if (a - b) * i % m < 0:  # to handle negative results
        k = m + (a - b) * i % m
    else:  # to handle positive results
        k = (a - b) * i % m
    # x=b+nk(mod mn)
    if b + n * k % mn < 0:  # to handle negative results
        x = mn + b + n * k % mn
    else:  # to handle positive results
        x = b + n * k % mn
    return x

# calculates modular inverse
# can be removed if not being used
def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if a * x % m == 1:
            return x
    return 1

# Converts a string into a hexadecimal representation of that string using the ASCII table values
def hexconv(inputt):
    hexchar = ""
    for x in range(len(inputt)):
        hexchar = hexchar + ("%X" % ord(inputt[x]))  # ord() converts characters to their ASCII decimal values
        # uses string formatting argument specifier %X to convert the decimal ASCII 
        # representation of the character to a hex value
    return hexchar

# Converts a string from hexadecimal representation to a string of characters
def decconv(inputt):
    decchar = ""
    for x in range(0, len(inputt) - 1, 2):
        decchar = decchar + chr(todeci(inputt[x] + inputt[x+1]))
    return decchar

# Calculates the change of base from hex to dec
def todeci(str):
    llen = len(str)
    power = 1
    num = 0
    for i in range(llen - 1, -1, -1):
        if val(str[i]) >= 16:
            print('Invalid number')
            return -1
        num += val(str[i]) * power
        power = power * 16
    return num

# helper function of todeci()
def val(c):
    if '0' <= c <= '9':
        return ord(c) - ord('0')
    else:
        return ord(c) - ord('A') + 10

# Test code for this module
"""
inputt = "Hello, world."
print(inputt)
somecrap = garbageGen(1000)
toencrypt = concatGarbageAndFlags(inputt, somecrap)
print(toencrypt)
hexmess = hexconv(toencrypt)
print(hexmess)
decmess = decconv(hexmess)
print(decmess)
afterencrypt = retrieveText(decmess)
print(afterencrypt)
"""
