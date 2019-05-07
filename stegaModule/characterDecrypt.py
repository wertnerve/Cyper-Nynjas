from PIL import Image
try:
    from stegaModule import VigenereCipher
    from stegaModule import EncryptionUtilities
except:
    import VigenereCipher
    import EncryptionUtilities
#
def decrypt(encryptedImage,password):
    eu = EncryptionUtilities
    startFlagFound=False
    endFlagFound=False

    # first, get pixelBuffer by getting last character of password
    pixelBuffer = password[len(password) - 1]
    pixelBuffer = int(pixelBuffer)
    print(pixelBuffer)

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
    textLength = int(abs(rgbValue[0]-rValueMod))
    print("Retrieved textlength:",textLength)
    
    pX=1
    pY=1

    #store decrypted text here
    decryptedCipherText=[]
    
    #while startFlagFound == False:
    while textLength > 0:
     pixelXY='('+str(pX)+','+str(pY)+')'
     print("Current pixel location (x,y) is",pixelXY)
     print("RGB value:",ePixels[pX,pY])
 
     rgbValue = list(ePixels[pX,pY])
     placeHolderRGB= list(ePixels[pX-1,pY])
     rValueMod = placeHolderRGB[0]
     difference = rValueMod-rgbValue[0]
     print("RGB value difference from left adjacent pixel is",difference)
     # get the vignere characters ASCII value and store it in list
     ASCII = difference
     print("Retrieved Vignere value:",[ASCII],"as a char =",chr(ASCII))
     vFlag = VigenereCipher.applyCipher(eu.getMessageFlag(1),password)
     print("Checking if ASCII =", vFlag)

     if [ASCII] is VigenereCipher.decryptCiphertext(vFlag,password):
         print("START FLAG AHS BEEN FOUND!")
         startFlagFound = True
     if startFlagFound or startFlagFound==False: decryptedCipherText.append(ASCII)

     # move to the next pixel in column(AKA x), if all pixels in the row have been reached, jump to next row
     try:
         pX += pixelBuffer
         print(ePixels[pX, pY])
     except:
         print("jumping to next row")
         pX = 1
         pY += 1

     textLength-=1

    print()
    print("Decrypted Vignere ciphertext:",decryptedCipherText)
    #throw it into the vignere decryptor!
    #for vignere decrypt need int array
   # password = EncryptionUtilities.convertToIntegerList(password)
    print("password",(password))
    plaintext = VigenereCipher.decryptCiphertext(decryptedCipherText,''.join(password))
    print("Decrypted plaintext:", plaintext)
    return (plaintext)

