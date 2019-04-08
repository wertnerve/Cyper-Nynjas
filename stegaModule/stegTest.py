from stegaModule import characterEncrypt
from stegaModule import characterDecrypt

#test

characterEncrypt.encrypt("apple.jpg","BEHOLD THE LAMB OF GOD!!",'9')
characterDecrypt.decrypt("encryptedImage.png",'9')