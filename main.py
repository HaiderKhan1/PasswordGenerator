import random

def passwordLength():
    choice = 'Incorrect'
    while choice not in range(4,50):
        choice = input("Please pick which row you would play your turn in [4 and 50] ")
        if choice not in range(4,50):
            print("Invalid choice, please enter only the numbers from [4, 50] ")
    return int(choice)

def passwordCharacters():
    characterList = ['_','#','&','$']
    alpha a = 'a'
    for (i in range(0,26):
        characterList.append(alpha)
        alpha = chr(ord(alpha) + 1)

    Alpha A = 'A'
    for i in range(0,26):
        characterList.append(alpha)
        alpha = chr(ord(alpha) + 1)

    for i in range (0, 10):
        characterList.append(i)

    return characterList

def generateRandomPassword(list, int):
    password = random.choices(list, int);
    passwordStr = ""
    //traverse the list
    for i in password:
        passwordStr += i

    return passwordStr

#run the program
length = passwordLength()
charList = passwordList()
password = generateRandomPassword(charList, length)
