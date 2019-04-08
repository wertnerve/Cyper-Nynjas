from PIL import Image
#for now this does not do anything
from stegaModule import globalVariables

def encrypt(image, text, pixelBuffer):
    # convert text to list of characters

    characterList = list(text)
    print(characterList)
    # include key for message in the message itself during encryption
    # load image
    img = Image.open(image)
    pixels = img.load()

    print("Image dimensions", img.size)
    print("Length:", len(characterList))
    print("Space between pixels:",pixelBuffer)
    print("Total number of pixels needed:",len(characterList)*pixelBuffer)
    lengthOfText = len(characterList)
    lengthOfText = int(lengthOfText)
    #check is there's enough pixels for the text to be encrypted, first row is reserved for pixelbuffer
    if lengthOfText*pixelBuffer > img.size[0]*img.size[1] :
        print("THERE ARE NOT ENOUGH PIXELS AVAILABLE FOR THIS TEXT")
        return 0
    else :
        print("REJOICE! THERE ARE ENOUGH PIXELS")
    # store the length of the text with two pixels
    #the first pixel copies the value of the second
    #then the r value of that pixels rbg value becomes r-length
    #do this under the abs() function in case length > r
    #during decrpyt, take the difference in r of both pixels
    print("Value of pixel before storing length:", pixels[0, 1])
    pixels[0,0] = pixels [1,0]
    placeHolderRGB = list(pixels[1,0])
    r = placeHolderRGB[0]  # original value
    g = placeHolderRGB[1]
    b = placeHolderRGB[2]
    r = abs(r-len(characterList))
    pixels[0,0] = (r,g,b)

    print("Value of pixel after stroing length:",pixels[1,0])

    # pixel x/y, start off at the second row, first column
    pX = 1 #start at one since 0 needs to be the placeholder(0 is the first pixel in the row, 1 is the second)
    pY = 1 #start at second row just to avoid overriding the length and to keep the encrypted pixel bitmap consistent

    # pixel selection process relies on pixelbuffer and the left adjacent pixel to each chosen pixel
    # pixellBuffer = passed in variable, last character of password, which is between 0-9
    # store characters on each row, with pixelBuffer lenght inbetween
    for char in characterList:
        # collect color value of current pixel, cast to list
        rgbValue = list(pixels[pX, pY])

        r = rgbValue[0]  # original value
        g = rgbValue[1]
        b = rgbValue[2]

        placeHolder = list(pixels[pX - 1, pY])  # r value from adjacent pixele
        placeHolder = placeHolder[0]

        r = placeHolder - ord(char)  # new value(adjacent pixel's value - char's ASCII value

        pixels[pX, pY] = (r, g, b)
        pixelXY = '(' + str(pX) + ',' + str(pY) + ')'
        print("Current pixel location (x,y) is", pixelXY)
        print("RGB value before adding", char, "=", rgbValue)
        print("RGB value after adding", char, "=", pixels[pX, pY], '\n')

        # move to the next pixel in column(AKA x), if all pixels in the row have been reached, jump to next row
        try:
            pX += pixelBuffer
            print(pixels[pX,pY])
        except:
            print("jumping to next row")
            pX = 1
            pY += 1

    # after all characters are encrpyted, show original and encrypted image!
    img.show()
    img.save("encryptedImage.png")
    eImage = Image.open("encryptedImage.png")
    eImage.show()
