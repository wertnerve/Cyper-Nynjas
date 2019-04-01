from PIL import Image


# three main variables, the image, the length of ciphertext, the time between row jumps
# potential idea, conjoin tL and rJT into one varibale, that can serve as password
def decrypt(encryptedImage, textLength, rowJumpTimer):
    encryptedImage = Image.open('encryptedImage.png')
    ePixels = encryptedImage.load()

    pX = 100
    pY = 100
    decryptedText = []

    while textLength > 0:
        pixelXY = '(' + str(pX) + ',' + str(pY) + ')'
        print("Current pixel location (x,y) is", pixelXY)
        print("RGB value:", ePixels[pX, pY])

        rgbValue = list(ePixels[pX, pY])
        placeHolderRGB = list(ePixels[pX - 1, pY])
        rValueMod = placeHolderRGB[0]
        # get the characters ASCII value and store it in list
        ASCIIchar = chr(rValueMod - rgbValue[0])
        print("Retrieved character:", ASCIIchar)
        decryptedText.append(ASCIIchar)

        pX += 100
        rjtPlaceholder = rowJumpTimer
        rowJumpTimer -= 1
        if rowJumpTimer == 0:
            pX = 100
            pY += 100
            rowJumpTimer = rjtPlaceholder
        textLength -= 1

    # return array of characters in string form
    return ''.join(decryptedText)
