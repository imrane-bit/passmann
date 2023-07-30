from cryptography.fernet import Fernet
import sys 


def decrypt_file(encryptedfile , keyfile):
    
    with open(keyfile , 'rb') as keyfile:
        seckey = keyfile.read()
        keyfile.close()


    with open(encryptedfile, 'rb') as encfile:
        data = encfile.read()
        decrypted = Fernet(seckey).decrypt(data)
        encfile.close()


    with open(encryptedfile, 'wb') as encfile :
        encfile.write(decrypted)
        encfile.close()


    
