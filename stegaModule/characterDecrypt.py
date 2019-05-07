
import VigenereCipher
import EncryptionUtilities
#import gui
try:
    from PIL import Image
except:
    import Image

def decrypt(encryptedImage,password):
    eu = EncryptionUtilities
    vc = VigenereCipher
    #variable for encryptedFlag, if incorrect pasword entered, extra garbage variables produced 
    flagList = list(eu.getMessageFlag(2))
    flagList = vc.applyCipher(flagList, password)
    flagList=''.join(str(c) for c in flagList)
    print("Looking for encyrpted flag =",flagList)
    startFlagFound=False
    endFlagFound=False

    # first, get pixelBuffer by getting last character of password
    pixelBuffer = password[len(password) - 1]
    pixelBuffer = int(pixelBuffer)
    print(pixelBuffer)

    eImage = Image.open(encryptedImage)
    ePixels = eImage.load()
    print("Dimensions",eImage.size)
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
   
    pX=0
    pY=0

    #store decrypted text here
    decryptedCipherText=[]
    pixelNum = eImage.size[0]*eImage.size[1]
    #while pixelNum != 0:
    width, heigh = eImage.size
    #try to incorperate .find method for start and end flag
    textLength = 1000
    while textLength > 0:
      pixelXY='('+str(pX)+','+str(pY)+')'
      #print("Current pixel location (x,y) is",pixelXY)
      #print("RGB value:",ePixels[pX,pY])
      rgbValue = list(ePixels[pX,pY])
      placeHolderRGB= list(ePixels[pX-1,pY])
      rValueMod = placeHolderRGB[0]
      difference = rValueMod-rgbValue[0]
       #    print("RGB value difference from left adjacent pixel is",difference)
       # get the vignere characters ASCII value and store it in list
      ASCII = difference
      #print("Retrieved Vignere value:",[ASCII],"as a char =",chr(ASCII))
       #  vFlag = VigenereCipher.applyCipher(eu.getMessageFlag(1),password)
       #print("Checking if ASCII =", vFlag)
      decryptedCipherText.append(ASCII)
      cipherTextString = ''.join(str(c) for c in decryptedCipherText)
      #check if end flag has been reached
      if cipherTextString.find(flagList) != -1 :
          print("FOUND ENDFLAG, EXITING LOOP")
          break
      #does not work, need to rework
      """
      #check if end flag has been reached
      if flagList in decryptedCipherText:
           print("END FLAG FOUND, EXITING LOOP")
           break
       
      """

       # move to the next pixel in column(AKA x), if all pixels in the row have been reached, jump to next row
      #pX += pixelBuffer
      pX+=2
      if pX >= eImage.size[0]:
        print("jumping to next row")
        pX = 1
        pY += 1

      textLength-=1
     
     #need line here to break after last pY is hit

    print()
    #print("Decrypted Vignere ciphertext:",decryptedCipherText)
    #throw it into the vignere decryptor!
    #for vignere decrypt need int array
   # password = EncryptionUtilities.convertToIntegerList(password)
    print("password",(password))
    print("Decrypted Vignere")
    plaintext = VigenereCipher.decryptCiphertext(decryptedCipherText,''.join(password))
    print("Decrypted plaintext with flags and garbage:", plaintext)
    plaintext=EncryptionUtilities.retrieveText(plaintext)
    message = "Decrypted plaintext:", plaintext
    #gui.printAlert("Message", plaintext)
    return (plaintext)

