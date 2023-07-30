from cryptography.fernet import Fernet
import sys


def encrypt_file(file):
    #try :
    key = Fernet.generate_key()

    with open('key.key','wb') as keyfile :
        keyfile.write(key)
        keyfile.close()
    fernet = Fernet(key)


    with open(file, 'rb') as f:
        content = f.read()
        f.close()
    encrypted = fernet.encrypt(content)
    with open(file, 'wb') as f :
        f.write(encrypted)
        f.close()

    #except Exception as e:
      #  print(e)
