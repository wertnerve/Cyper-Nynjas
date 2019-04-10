from stegaModule import characterEncrypt
from stegaModule import characterDecrypt
from stegaModule import VigenereCipher

#characterEncrypt.encrypt("apple.jpg","There's no time! We have to get ~$10,000 by 12:00 A.M. tomorrow ehrbf3847h+_=*^&(*&^%$%^&U*I!~?><>",'1234')
characterEncrypt.encrypt("apple.jpg","JEFF!",'1234')
characterDecrypt.decrypt("encryptedImage.png",'1234')

