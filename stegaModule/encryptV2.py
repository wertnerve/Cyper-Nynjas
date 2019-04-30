from PIL import Image
import EncryptionUtilities
import VigenereCipher
import characterDecrypt
#for now this does not do anything


def encrypt(image, text, password):

    eu = EncryptionUtilities
    #print(text)
    #size of what we can - size of text - size of characters for flag is the number you pass
    #to garbage gen(x), it will geenrate that many chaarcters

    #split it somewhere random, or down the middle
    #now we need to add garbage

  
    # include key for message in the message itself during encryption
    # load image
    img = Image.open(image)
    pixels = img.load()
    #first, get pixelBuffer by getting last character of password
    pixelBuffer = eu.getPixelBuffer(password)
   
    garbageCharNum = (img.size[0]*img.size[1])-len(text)
    garbageCharNum -= eu.getMessageFlagLength()
    garbageCharNum = garbageCharNum // pixelBuffer
    print("Image dimensions", img.size)
    print("Total number of pixels :",img.size[0]*img.size[1])
    print("Length of plaintext:", len(text))
    print("Space between pixels:",pixelBuffer)
    garbageCharNum=100
    print("Total # of garbage characters==",garbageCharNum)
#   GARBAGE WILL BE FULLY ADDED LATER, FOR NOW GABRAGE IS CAPPED AT 1000
    print("plaintext:",text)
    text = eu.concatGarbageAndFlags(text,eu.garbageGen(garbageCharNum))
    print("Length of plaintext after adding flags and garbage:",len(text))
    print("Total number of pixels needed:",len(text)*pixelBuffer)

    lengthOfText = len(text)
    #check is there's enough pixels for the text to be encrypted, first row is reserved for pixelbuffer
    if lengthOfText*pixelBuffer > img.size[0]*img.size[1] :
        print("THERE ARE NOT ENOUGH PIXELS AVAILABLE FOR THIS TEXT")
        return 0
    else :
        print("REJOICE! THERE ARE ENOUGH PIXELS")        
         #before anything else, throw the plaintext into the Vigenere Cipher!
        print("plaintext as char list")
        # convert ciphertext to list of characters
        characterList = list(text)
        print(characterList)

        print("plaintext AFTER VIGNERE ENCRYPTION:")
        text = VigenereCipher.applyCipher(text, password)
        print(text)
        print("Ciphertext as character list")
        characterList = list(text)
    """
    # store the length of the text with two pixels
    #the first pixel copies the value of the second
    #then the r value of that pixels rbg value becomes r-length
    #do this under the abs() function in case length > r
    #during decrpyt, take the difference in r of both pixels
    pixels[0,0] = pixels [1,0]
    placeHolderRGB = list(pixels[1,0])
    r = placeHolderRGB[0]  # original value
    g = placeHolderRGB[1]
    b = placeHolderRGB[2]
    r = abs(r-len(characterList))
    pixels[0,0] = (r,g,b)
    
    """
    # pixel x/y, start off at the second row, first column
    pX = 0 #start at one since 0 needs to be the placeholder(0 is the first pixel in the row, 1 is the second)
    pY = 0 #start at second row just to avoid overriding the length and to keep the encrypted pixel bitmap consistent

    # pixel selection process relies on pixelbuffer and the left adjacent pixel to each chosen pixel
    # pixellBuffer = passed in variable, last character of password, which is between 0-9
    # store characters on each row, with pixelBuffer lenght inbetween
    curr = 0
    for char in characterList:
       # print()
     curr+=1
     #print(pX,pY)
        # collect color value of current pixel, cast to list
     rgbValue = list(pixels[pX, pY])

     r = rgbValue[0]  # original value
     g = rgbValue[1]
     b = rgbValue[2]
     placeHolder = list(pixels[pX - 1, pY])  # r value from adjacent pixele
     placeHolder = placeHolder[0]
      #  print(placeHolder)
       # print(char)
       # print("Storing",char, "ASCII value:",chr(char))
     r = placeHolder - char
     #   r = placeHolder - ord(char)  # new value(adjacent pixel's value - char's ASCII value
    
     pixels[pX, pY] = (r, g, b)
     pixelXY = '(' + str(pX) + ',' + str(pY) + ')'
     """
     if curr < 10:
      print("Current pixel location (x,y) is", pixelXY)
      print("RGB value before adding", char, "=", rgbValue)
      print("RGB value after adding", char, "=", pixels[pX, pY], '\n')
     """
        # move to the next pixel in column(AKA x), if all pixels in the row have been reached, jump to next row

    # try:
     #pX += pixelBuffer
     pX+=2
     if pX >= img.size[0]:
        print("jumping to next row")
        pX = 1
        pY += 1
           # print(pixels[pX,pY])
    """
     except IndexError:
            
     """

    # after all ciphertext characters are encrpyted, show original and encrypted image!
    #img.show()
    print(image)
    filename = EncryptionUtilities.trimFilename(image)
    filename+="encryptedImage.png"
   # filename = "encryptedImage.png"
    img.save(filename)
    eImage = Image.open(filename)
    #test if decryption works
    
    print("Encryption Succesfull!")
    print(filename)
    #eImage.show()
