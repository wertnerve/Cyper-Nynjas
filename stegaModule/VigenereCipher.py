"""
This method will apply a Vigenere cipher to a message that is passed in as either a file name or a string.
The Vigenere cipher works just like a Caesar (shift) cipher, except it uses a codeword of length n to
shift each letter within chunks of size n of the message by the value of each letter in the codeword.
For instance, given message "hello" and codeword "dog", "h" will be shifted by "d", "e" will be shifted by "o",
"l" will be shifted by "g", "l" will be shifted by "d", and lastly "o" will be shifted by "o". A list containing
the encrypted characters will be returned, which will make it easier to iteratively encode each character into
the image.
"""

def applyCipher(message, word):
    #Check whether the value passed into the message parameter is a text file name, or a string.
    try:
        myFile = open(message, "r")
        plaintext = myFile.read().replace('\n', ' ')
        myFile.close()
    except:
        plaintext = message

    ptChars = list(plaintext) #Divide the message into individual characters
    ptASCII = list() #Will hold the ASCII values of our plaintext characters
    for x in ptChars:
        ptASCII.append(ord(x)) #Adds the ASCII value of each character to the empty list

    #This section of the method works the same as the section above
    cipherWord = word
    cipherChars = list(cipherWord)
    cipherASCII = list()
    for x in cipherChars:
        cipherASCII.append(ord(x))

    n = len(cipherWord)
    encryptedChars = list() #Define a list to hold our encrypted characters
    k = 0
    for x in range(len(ptASCII)): #Gives index values for each element in our list of plaintext ASCII values
        y = x % n #Finds location in cipherASCII that corresponds to current location in ptASCII list
        ASCIIsum = int(ptASCII[x]) + int(cipherASCII[y])
        encryptedChars.append(ASCIIsum % 127) #Mod by 127 because ASCII uses values 0-127
    print(encryptedChars)
    return encryptedChars


#This method will work just like the one above, but instead of encrypting the characters at the end
#it will decrypt them by subtracting the corresponding codeword ASCII value from the ciphertext ASCII value,
#and computing the answer mod 127. A list containing the encrypted

def decryptCiphertext(encryptedText, cipherword):

    if hasattr(encryptedText, "open"):
        with open(encryptedText, "r") as myFile:
            ciphertext = myFile.read().replace('\n', '')

    elif hasattr(encryptedText, "append"):
        ciphertext = encryptedText

    else:
        ciphertextString = encryptedText
        #ciphertext = string_splitting_function(ciphertextString) (return type: list)
        #will have to work on a way to split a string of ints representing ASCII values into
        #a list of coherent values

    codewordChars = list(cipherword)
    decryptedChars = list()
    n = len(cipherword)
    for x in range(len(ciphertext)):
        y = x % n
        ASCIIdiff = ciphertext[x] - ord(codewordChars[y])
        decryptedChars.append(ASCIIdiff % 127)
    print (decryptedChars)
    decryptedMessage = ""
    for a in decryptedChars:
        decryptedMessage += chr(a)
    return decryptedMessage

testfile = "VigenereCipherTest.txt"
encryptedCharList = applyCipher(testfile, "ciph")
decryptedMessage = decryptCiphertext(encryptedCharList, "ciph")
print (decryptedMessage)