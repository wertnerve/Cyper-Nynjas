from PIL import Image


def encrypt(image, text, rowJumpTimer):
    # convert text to list of characters
    characterList = list(text)
    print(characterList)

    # include key for message in the message itself during encryption
    # load image
    img = Image.open(image)
    pixels = img.load()
    print("Image dimensions", img.size)

    pixelBufferX = 100  # space between affected columns
    pixelBufferY = 100  # same as pBx, but for rows

    # pixel x/y, start off at 100,100
    pX = 100
    pY = 100
    rjtPlaceholder = rowJumpTimer
    # iterate every 100th pixel
    # store 10 characters on each row, spaced 100 pixel between each
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

        # move to the next pixel in column(AKA x), after 10 column shifts, go to next row(AKA y)
        pX += 100
        rowJumpTimer -= 1
        if rowJumpTimer == 0:
            pX = 100
            pY += 100
            rowJumpTimer = rjtPlaceholder
    # after all characters are encrpyted, show image!
    img.show()
    img.save("encryptedImage.png")
