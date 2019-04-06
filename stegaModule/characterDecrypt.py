from PIL import Image
#three main variables, the image, the length of ciphertext, the time between row jumps
#potential idea, conjoin tL and pbPlaceholder into one varibale, that can serve as password
#removed textLength, thats done locally since length has been stored in first pixel
def decrypt(encryptedImage,pixelBuffer):


    eImage = Image.open(encryptedImage)
    ePixels = eImage.load()

    rgbValue = list(ePixels[0,1])
    placeHolderRGB= list(ePixels[0,0])
    rValueMod = placeHolderRGB[0]
    #get the characters ASCII value and store it in list
    textLength = int(rValueMod-rgbValue[0])
    print("Retrieved textlength:",textLength)
    
    pX=10
    pY=10
    decryptedText=[]
    
    while textLength >0:
     pixelXY='('+str(pX)+','+str(pY)+')'
     print("Current pixel location (x,y) is",pixelXY)
     print("RGB value:",ePixels[pX,pY])
 
     rgbValue = list(ePixels[pX,pY])
     placeHolderRGB= list(ePixels[pX-1,pY])
     rValueMod = placeHolderRGB[0]
     #get the characters ASCII value and store it in list
     ASCIIchar = chr(rValueMod-rgbValue[0])
     print("Retrieved character:",ASCIIchar)
     decryptedText.append(ASCIIchar)
     
     pX+=10
     pbPlaceholder = pixelBuffer
     pixelBuffer-=1
     if pixelBuffer==0:
          pX=10
          pY+=10
          pixelBuffer=pbPlaceholder
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
