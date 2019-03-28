from PIL import Image
#three main variables, the image, the length of ciphertext, the time between row jumps
#potential idea, conjoin tL and rJT into one varibale, that can serve as password
def decrypt(encryptedImage,textLength,rowJumpTimer):
    ePixels = encryptedImage.load()
    
    pX=100
    pY=100
    decryptedText=[]
    
    while textLength >0:
     pixelXY='('+str(pX)+','+str(pY)+')'
     print("Current pixel location (x,y) is",pixelXY)
     print("RGB value:",ePixels[pX,pY])
 
     rgbValue = list(ePixels[pX,pY])

     #get the characters ASCII value and store it in list
     ASCIIchar = chr(255-rgbValue[0])
     print("Retrieved character:",ASCIIchar)
     decryptedText.append(ASCIIchar)
     
     pX+=100
     rowJumpTimer-=1
     if rowJumpTimer==0:
          pX=100
          pY+=100
          rowJumpTimer=10
     textLength-=1
     
    #return array of characters in string form
    return ''.join(decryptedText)
    

#reference on how to iterate eveyr pixel in image
#for x in range(encryptedImage.size[0]): #even column of pixels
 #   for y in range(encryptedImage.size[1]):

textLength = 4
rowJumpTimer = 10 #timer for how many pixels per row are inspected before jumping to next row
plaintext=decrypt(Image.open('encryptedImage.png'),textLength,rowJumpTimer)
print()
print("Decrypted text:",plaintext)

       

