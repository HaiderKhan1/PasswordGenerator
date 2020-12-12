import random

def passwordLength():
    choice = "Incorrect"
    numChoice = 0
    while numChoice not in range(4,20):
        choice = input("Chose your password length [4 and 20] ")
        numChoice = int(choice)
        if numChoice not in range(4,20):
            print("Invalid choice, please enter only the numbers from [4, 20] ")
    return numChoice

def passwordCharacters():
    characterList = ['_','#','&','$']
    alpha = 'a'
    for i in range(0,26):
        characterList.append(alpha)
        alpha = chr(ord(alpha) + 1)

    Alpha = 'A'
    for i in range(0,26):
        characterList.append(Alpha)
        Alpha = chr(ord(Alpha) + 1)

    for i in range (0, 10):
        characterList.append(i)

    return characterList

def generateRandomPassword(passList, n):
    password = random.choices(passList, n)
    passwordStr = ""
    return (passwordStr.join(password))

#run the program
length = passwordLength()
#print(length)
charList = passwordCharacters()
#print(charList)
password = generateRandomPassword(charList, length)
print(password)
