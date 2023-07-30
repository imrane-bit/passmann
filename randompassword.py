import random 
import string
import sys




def generate_password(lenofpass):
    #till now we will just declare the password and password length variables
    password = ""
    lenght = int(lenofpass) #int(input("password length (more than or equal 14):"))


    #for evry time the for loop repeats 
    #we want to append a new random lowercase,uppercase or a number to the password
    #so the characaters order generated by this algorithm won't be predictable

    if lenght >= 14 :
        for i in range(int(lenght)):
            # declaring random vallues everytime the loop stars 
            lowercasestr = chr(random.randint(ord('a'),ord('z')))
            uppercasestr = chr(random.randint(ord('A'),ord('Z')))
            numberstr = chr(random.randint(ord('0'),ord('9')))
            n = random.randint(1,len(list(string.punctuation)))
            specialcharstr = list(string.punctuation)[n-1]

            #putting them in a list so we can randomise when appending them
            randlist = [numberstr,uppercasestr,lowercasestr,specialcharstr]
            #appending random one of them to the password 
            password += randlist[random.randint(0,3)]
        
        
        return password
    else :
        print("password length must be at least %i characters",8)