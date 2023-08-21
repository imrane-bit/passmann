#!/usr/bin/env python3
import encrypt
import decrypt
import randompassword
import csv
import shutil
import os , subprocess
from pathlib import Path
import sys
#this is the first usefull program i made xd
#the modules encrypt and decrypt and randompassword are made by me , the decrypt and encrypt scripts are just udsing the cryptography library so no need for documentation
#the randompassword script is documented

'''def check():
    #checking if the user has root access
    user = os.getenv("SUDO_USER")
    if user is None:
        print ("this script needs root privileges to run")
        exit()
    else:
        userpanel()'''


#there will be a file named whitehouse.csv encrypted with the a key named key.key by the module encrypt
#when needed the function will decrypt the file , so we can do the oppertions requested by the user



#this functions stands for searching by comparing the arg with all the acounts information 
#so the user can search by username, password,platform and also email
#it will be user after to display the acounts of a specific platform (or with a pass or user etc) if given as a command line argument



#path to white house file
path1 = "/home/YOUR_USER/.passmann/white house.csv"
#path to key
path2 = "/run/media/YOURUSER/YOURUSBNAME/passmannkey/key.key"
#path to the key folder
path3 = "/run/media/YOURUSER/YOURUSBNAME//passmannkey"
def searchfunc(searchkeyword):
    decryptwh()

    with open(path1,"r+") as File :
        reader = csv.reader(File)    
        i = 0
        for row in reader :
            if searchkeyword.upper() in row[0].upper()  or searchkeyword.upper() in row[1].upper() or searchkeyword.upper() in row[3].upper() or searchkeyword.upper() in row[2].upper():
                print("-----------------------------------------------------------------------\n ")
                print(f"{i})  platform   : {row[0]} \n     username   : {row[1]} \n     email      : {row[3]} \n     password   : {row[2]} \n \n")
                print("-----------------------------------------------------------------------\n ")
                
                i += 1
                continue
            else :
                i += 1
                continue
    encryptwh()
    File.close()






def decryptwh():
    try : 
        
        decrypted = decrypt.decrypt_file( path1, path2)
        os.remove(path2)
    except Exception as e:
        print(e)
        return


#there will be a file named whitehouse.csv but now decrypted
#when needed this function will encrypt the file and return the encrypted file (overwriting the original) , after we done the opperations the user requested
#the function will encrypt the file with a new generated key wich will also overwrite the original
 #opening the whitehouse.csv encrypted file

def encryptwh():
    try :
    
        encrypted = encrypt.encrypt_file(path1)
        src_path = r"key.key"
        dst_path = path3
        shutil.move(src_path, dst_path)


    except Exception as e :
        print(e)
        return


#making a home pannel the user can interact with so he call the funcs he wants


def userpanel():
    os.system('clear')
    
    while True:
        print("Welcome to the home pannel")
        print("1.  see your accounts")
        print("2.  see a specific account by number")
        print("3.  add account to the manager")
        print("4.  delete account from the manager")
        print("5.  update an account ")
        print("6.  genrate Random Password")
        print("7.  decrypt the passwords file")
        print("8.  encrypt the passwords file")
        print("9.  search for accounts using keyword")
        print("10. make backup ")
        print("11. restore backup ")
        print("12. close")
        try:
            choice = int(input("Enter a number :"))
        except ValueError as ver:
            print(ver)
            continue

    #processing the user’s choice
        if choice == 1:
            os.system('clear')
            seeaccounts()
        elif choice == 2:
            os.system('clear')
            seeaccount()
        elif choice == 3:
            addaccount()
        elif choice == 4:
            os.system('clear')
            deleteacc()
        elif choice == 5:
            os.system('clear')
            modifyacc()
        elif choice == 6:
            randompassworddd()
        elif choice == 7:
            decryptwh()
        elif choice == 8:
            os.system('clear')
            encryptwh()
        elif choice == 9:
            os.system('clear')
            print("NOTE : the search keyword is more than one word , put it into quotes like that : 'example'")
            keyword = input( "enter the search keyword : ")
            os.system('clear')
            searchfunc(keyword)            
        elif choice == 10 :
            makebackup()
        elif choice == 11 :
            getbackup()
        elif choice == 12:
            os.system('clear')
            break
        else:
            print("Wrong choice")
            continue



#this will be a function to make backups 
def makebackup():
    with open(path1 , "r") as original , open("/home/imranebit/.passmann/.backup/white house.csv" , 'w') as backup :
         origreader = csv.reader(original)
         backwriter = csv.writer(backup)
         backwriter.writerows(origreader)
         original.close()
         backup.close()

    with open("/run/media/imranebit/Ventoy/passmannkey/key.key" , "r") as original , open("/run/media/imranebit/Ventoy/passmannkey/.backup/key.key" , 'w') as backup :
         origreader = original.read()
         backup.write(origreader)
         original.close()
         backup.close()

#this function is responsible of recovering backups
def getbackup():
    with open(path1 , "w") as original , open("/home/imranebit/.passmann/.backup/white house.csv" , 'r') as backup :
         backupreader = csv.reader(backup)
         origwriter = csv.writer(original)
         origwriter.writerows(backupreader)
         original.close()
         backup.close()

    with open("/run/media/imranebit/Ventoy/passmannkey/key.key" , "w") as original , open("/run/media/imranebit/Ventoy/passmannkey/.backup/key.key" , 'r') as backup :
         backupreader = backup.read()
         original.write(backupreader)
         original.close()
         backup.close()



#this function will be responsible of decrypting and adding the accounts to the passwordsfile and then encrypting it again with a new encryption key
def addaccount():
    os.system('clear')
    #gettin the infos from the user
    username = input("Enter the username the account : ")
    password = input("Enter the password of the account : ")
    platform = input("Enter the platform link or name : ")
    email = input("Enter the email the account : ")
    data = [platform , username, password,email]
    #adding the account
    decryptwh()
    with open(path1,"a") as decfile :
        writer = csv.writer(decfile)
        writer.writerow(data)
    os.system('clear')
    print("Account added successfully")
    encryptwh()



#this function will be responsible of generating passwords using the module randompassword.py wich i made before , it is documented , take a look at it for more details
def randompassworddd():
    while True :
        try :
            len = int(input("Enter the lenght of the password you want :"))
            pasword = randompassword.generate_password(len)
            os.system('clear')
            print(f"\n\nthe password : {pasword}\n\n")
            break
        except Exception as e :
            print(e)
            continue




# this function will show the user all of his accounts and their passwords by decrypting the passwordsfile getting the values from it and encrypting it again 
def seeaccounts():
    decryptwh()
    
 #printing the accounts with unique numbers so the user can edit/delete them later by specifiying the number   
    with open(path1, "r") as decryptedf :
        csv.reader(decryptedf)
        reader = csv.reader(decryptedf)

        i = 0
        for row in reader:
            print("-----------------------------------------------------------------------\n ")
            print(f"{i})  platform   : {row[0]} \n     username   : {row[1]} \n    email       : {row[3]} \n    password    : {row[2]} \n \n")
            i += 1
        encryptwh()


#this function will allow the user to see a specific account by entering the number of it .abs

def seeaccount():
    
    choice = int(input("enter the account number: "))
    decryptwh()

    with open(path1,"r+") as File :
        reader = csv.reader(File)    
        i = 0
        for row in reader :
            if i == choice :
                print("-----------------------------------------------------------------------\n ")
                print(f"{i})  platform   : {row[0]} \n     username   : {row[1]} \n     email      : {row[3]} \n     password   : {row[2]} \n \n")
                print("-----------------------------------------------------------------------\n ")
                encryptwh()
                File.close()
                return 
            else :
                i += 1
                continue



#this function is responsible of deleting specific accounts from the accounts file by decrypting the passwordsfile , deleting the account row  and encrypting it again 
def  deleteacc():
    while True:
        try:
            #showing the accounts to the user using the past functions with the unique numbers
            seeaccounts()
            choice = int(input("write the number of the account you want to delete :"))
            decryptwh()

            
            #creating a temporary file
            with open(path1,"r+") as inp, open("temp.csv" , "w") as out:
                inreader = csv.reader(inp)
                outwriter = csv.writer(out)
                i = 0
                #appending every row (account) from the originam to the temp file except the one selected by the user
                # that is done with matching the user's choice with the account with the same enumeration technique used to show the accounts and their numbers
                for row in  inreader:
                    if i != choice:
                        
                        outwriter.writerow(row)
                        
                    i += 1
            inp.close()
            out.close()

            #writing the temp file contents in original file (we delted the wanted row previously while appendind to the temp file)
            with open(path1,"w") as inp, open("temp.csv" , "r") as out:
                outreader = csv.reader(out)
                inwriter = csv.writer(inp)
            
                inwriter.writerows(outreader)
                inp.close()
                out.close()
            encryptwh()
            #removing the temp file
            os.remove("temp.csv")
            os.system('clear')
            print("account deleted")
            break
        except Exception as e:
            print(e)
            continue
        


 #this function is responsible of updating the password of a specific account in the accounts file by decrypting the passwordsfile, updating the password and encrypting it again
#it works pretty much like the delete function exept here instead of deleting the password we edit it 
def modifyacc() :
    while True :
        try :
            seeaccounts()
            choice = int(input("write the number of the account you want to update :"))
            decryptwh()
    
            with open(path1,"r+") as inp, open("temp.csv" , "w") as out:
                inreader = csv.reader(inp)
                outwriter = csv.writer(out)
                i = 0
                for row in  inreader:
                    if i == choice:
                        print("what do you want to change  : \n 1. username \n 2. email \n 3. password")
                        choicetwo = int(input("enter the number : "))
                        if choicetwo == 1 :
                            data = [row[0],input("write the new username :"),row[2],row[3]]
                            outwriter.writerow(data)
                            i += 1
                        elif choicetwo == 2 :
                            data = [row[0],row[1],row[2],input("write the new email :")]
                            outwriter.writerow(data)
                            i += 1
                        elif choicetwo == 3 :
                            data = [row[0],row[1],input("write the new password :"),row[3]]
                            outwriter.writerow(data)
                            i += 1
                    else:
                        outwriter.writerow(row)
                        i += 1
            inp.close()
            out.close()
    
            with open(path1,"w") as inp, open("temp.csv" , "r") as out:
                outreader = csv.reader(out)
                inwriter = csv.writer(inp)
                
                inwriter.writerows(outreader)
                inp.close()
                out.close()
            encryptwh()
            os.remove("temp.csv")
            os.system('clear')
            print("acccount updated")
            break
        except Exception as e:
            print(e)
            continue
        
#checking if the file exists or we should create it and encrypt it (happens in the first time only)
try :
    with open (path1, "r") as f:
        f.readlines()
        f.close()
except Exception as e:
    with open (path1, "w") as f:
        f.close()
    encryptwh()

try :
    plat = sys.argv[1]
    searchfunc(plat)
except :
    userpanel()
