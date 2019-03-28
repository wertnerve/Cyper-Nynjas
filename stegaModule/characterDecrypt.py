from PIL import Image

#load up encrypted image, this is hardcoded but will be changed once we begin connecting modules
encryptedImage = Image.open('encryptedImage.png')
ePixels = encryptedImage.load()
#hardcoded, simple pixel pointers
pX=100
pY=100
#hardcoded length of text
textLength = 4
decryptedText=[]
timeUntilNextRow=10
while textLength >0:
 pixelXY='('+str(pX)+','+str(pY)+')'
 print("Current pixel location (x,y) is",pixelXY)
 print("RGB value:",ePixels[pX,pY])
 
 rgbValue = list(ePixels[pX,pY])
 decryptedText.append(chr(255-rgbValue[0]))#get the characters ASCII value
 pX+=100
 timeUntilNextRow-=1
 if timeUntilNextRow==0:
          pX=100
          pY+=100
          timeUntilNextRow=10
 textLength-=1
print("Retrieved character array:")
print(decryptedText)
print("plaintext:",''.join(decryptedText))

       

