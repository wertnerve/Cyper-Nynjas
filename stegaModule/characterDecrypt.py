from PIL import Image
#not in use
#from stegaModule import globalVariables

#three main variables, the image, the length of ciphertext, the time between row jumps
#potential idea, conjoin tL and pbPlaceholder into one varibale, that can serve as password
#removed textLength, thats done locally since length has been stored in first pixel
def decrypt(encryptedImage,pixelBuffer):


    eImage = Image.open(encryptedImage)
    ePixels = eImage.load()
    #R stands for R for RGB
    #get the text length by taking the difference in R values
    print("0,1",ePixels[1,0])
    print("0,0",ePixels[0,0])
    rgbValue = list(ePixels[1,0])
    print(rgbValue[0])
    placeHolderRGB= list(ePixels[0,0])
    rValueMod = placeHolderRGB[0]
    print(rValueMod)
    #get the characters ASCII value and store it in list
    textLength = int(abs(rgbValue[0]-rValueMod))
    print("Retrieved textlength:",textLength)
    
    pX=1
    pY=1

    #store decrypted text here
    decryptedText=[]
    
    while textLength >0:
     pixelXY='('+str(pX)+','+str(pY)+')'
     print("Current pixel location (x,y) is",pixelXY)
     print("RGB value:",ePixels[pX,pY])
 
     rgbValue = list(ePixels[pX,pY])
     placeHolderRGB= list(ePixels[pX-1,pY])
     rValueMod = placeHolderRGB[0]
     difference = rValueMod-rgbValue[0]
     print("RGB value difference from left adjacent pixel is",difference)
     #get the characters ASCII value and store it in list
     ASCIIchar = chr(difference)
     print("Retrieved character:",ASCIIchar)
     decryptedText.append(ASCIIchar)

     # move to the next pixel in column(AKA x), if all pixels in the row have been reached, jump to next row
     try:
         pX += pixelBuffer
         print(ePixels[pX, pY])
     except:
         print("jumping to next row")
         pX = 1
         pY += 1

     textLength-=1
     
    #return array of characters in string form
    print()
    print("Decrypted text:",''.join(decryptedText))
    return (''.join(decryptedText))
    

#reference on how to iterate eveyr pixel in image
#for x in range(encryptedImage.size[0]): #even column of pixels
 #   for y in range(encryptedImage.size[1]):

#textLength = 10
#pixelBuffer = 10 #timer for how many pixels per row are inspected before jumping to next row
#plaintext=decrypt(Image.open('encryptedImage.png'),textLength,pixelBuffer)
#print()
#print("Decrypted text:",plaintext)
