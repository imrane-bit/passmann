# passmann


 - [General](#General) 
 - [Features](#Features) 
 - [Coming Features](#Coming-Features) 
 - [For more](#For-more) 
 - [comtact me](#comtact-me) 


 - ## general
- a terminal based password manager that stores all your password encrypted in your device,  encrypted with a key in your usb , it requires moving the key file to some usb or any external storage ,and editing the key file location in the script in order to work .
- ## Features
- ### 1. full encryption
- the files where the accounts are stored are completely encrypted , and cannot be seen unless the usb with the key is pluged in , but be carefull , DO NOT delete the whitehouse.csv from the  device or key.key file from the usb , the passes in this case are lost permanently.
-  the encryption key changes many time eveytime you run the programm for more protection.
- ### 2. basic features
- from a basic stand point the program gives the possibility of adding accouns , deleting them , editing them and of course seeing them .
- ### 3. more advanced features
- #### note : the accounts are indexed , each accounts have a specific number
- #### encrypting , decrypting manually
- the tool gives you the ablity to decrypt and encrypt your passwords file manually ,but be carefull , encrypting the file two times will cause the old key to be overwrriten , wich means you cannot restore your accounts but only restore a encrypted version.of them with no key . dont do that manually unless you know what are you doing .
- #### 4.showing specific account
- by entering the nember that a accounts is indexed with . you can veiw that specfic account .
- #### 5.command line arguments 
- in case of the  user giving a command line argument like that "python3 pssmann.py keyword" , it will automaticaty search for the keyword given in the passwords file nd show all the accounts containing this keyword as platform,email,username,password .
- ### 6. searching 
- the program provides the ability to search for a specfic keyword(email,pass,user,platform), same as before in commandline args , it will automaticaty search for the keyword given in the passwords file nd show all the accounts containing this keyword as platform,email,username,password .
- ### 7. generating strong passwords
- the tool provides a function that generates strong passwords , with the option of chosing the password-lenght
- ## Coming Features
- backup feature
- the folder with the accounts in it will  become hidden
- use of pgp keys
- more encryption 
- better design 
- ability to get an acount info by puting its index as command-line-argument
- automatic password copy
- ## For more 
- read the docummention in the scripts for more detailed stuff
- ## comtact me 
- if you have any concerns , please contact me at my email (i check it daily):
- imraneqbit@proton.me 
