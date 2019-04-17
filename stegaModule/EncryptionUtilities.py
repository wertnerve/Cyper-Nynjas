import math
import random

def garbageGen(x):
    garb = ""
    for i in range(x):
        char = chr(random.randint(32, 127))
        while (char == getMessageFlag(1) or char == getMessageFlag(2)):
            char = chr(random.randint(32, 127))
        garb = garb + char

    return garb

def getMessageFlag(x):
    if x == 1:
       return '('
    if x == 2:
        return ')'

def concatMessageFlags(text):

    return getMessageFlag(1)+text+getMessageFlag(2)

def trimFilename(text):
    x = len(text)-1
    char = text[x]
    while char is not '/':
        text=text[:-1]
        x = len(text)-1
        char = text[x]
    return text


def convertToIntegerList(x):
    y = []
    i = 0
    for char in x:
        y.append(int(x[i]))
        print(y)
        i += 1
    return y

def euclid_alg(a, b):
    """Performs the euclidean algorithm to determine the gcd of two integers"""
    r = 1
    while r is not 0:
        q = math.floor(a / b)
        r = a - b * q
        if r is 0:
            break
        a = b
        b = r
    return b


def mod_exp(y, x, n):
    """Performs modular exponentiation"""
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


def chin_rem_them(a, m, b, n):
    """Performs the Chinese Remainder Theorem"""
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


def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if a * x % m == 1:
            return x
    return 1


def hexconv(inputt):
    """Converts a string into a hexadecimal representation of that string using the ASCII table values"""
    hexchar = ""
    for x in range(len(inputt)):
        hexchar = hexchar + ("%X" % ord(inputt[x]))  # ord() converts characters to their ASCII decimal values
        """uses string formatting argument specifier %X to convert the decimal ASCII 
        representation of the character to a hex value"""
    return hexchar


def decconv(inputt):
    decchar = ""
    for x in range(0, len(inputt) - 1, 2):
        decchar = decchar + chr(todeci(inputt[x] + inputt[x+1]))
    return decchar


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


def val(c):
    if '0' <= c <= '9':
        return ord(c) - ord('0')
    else:
        return ord(c) - ord('A') + 10

"""
inputt = "Hello, world."
hexmess = hexconv(inputt)
decmess = decconv(hexmess)
print(inputt)
print(hexmess)
print(decmess)
"""
