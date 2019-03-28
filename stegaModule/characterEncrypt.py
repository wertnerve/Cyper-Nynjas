from PIL import Image

#get text and convert it to list of characters
text="my name is Jeff"
print("Text to encrypt:",text)
characterList=list(text)
print(characterList)

#load image 
img = Image.open("apple.jpg")
pixels = img.load()
print("Image dimensions",img.size)

pixelBufferX=100 #space between affected columns
pixelBufferY=100 # same as pBx, but for rows
#TEST 
#HOWDY!
#pixel x/y, start off at 100,100
pX=100
pY=100
px=200-100
timeUntilNextRow=10
#iterate every 100th pixel 
#store 10 characters on each row, spaced 100 pixel between each
for char in characterList:
     #collect color value of current pixel, cast to list
     rgbValue = list(pixels[pX,pY])
     
     r=rgbValue[0]
     g=rgbValue[1]
     b=rgbValue[2]
     
     pixelXY='('+str(pX)+','+str(pY)+')'
     print("Current pixel location (x,y) is",pixelXY)
     print("RGB value before adding",char,"=",rgbValue)
     
     r=r-ord(char)#change the red value by subtracting the characters ASCII Value
     pixels[pX,pY] = (r,g,b)
     
     print("RGB value after adding",char,"=",pixels[pX,pY],'\n')
     
     #move to the next column(x), after 10 column shifts, go to next row(y)
     pX+=100
     timeUntilNextRow-=1
     if timeUntilNextRow==0:
          pX=100
          pY+=100
          timeUntilNextRow=10
#after all characters are encrpyted, show image!       
#img.show()
img.save('encryptedImage.jpg')

