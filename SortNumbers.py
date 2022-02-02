#Name: Raymond J. Spieldenner
#Assignment: If Else - Project: Sorting Numbers
#Date: 02/01/2022

#Input Variables:

userInput1 = int(input('Please input first number: '))
userInput2 = int(input('Please input second number: '))
userInput3 = int(input('Please input third number: '))

#Finding the largest number:
if userInput1 > userInput2 and userInput1 > userInput3:
    print(userInput1)
elif userInput2 > userInput1 and userInput2 > userInput3:
    print(userInput2)
elif userInput3 > userInput1 and userInput3 > userInput2:
    print(userInput3)
#Finding the middle number:
if userInput1 > userInput2 and userInput1 < userInput3:
    print(userInput1)
elif userInput2 > userInput1 and userInput2 < userInput3:
    print(userInput2)
elif userInput3 > userInput1 and userInput3 < userInput2:
    print(userInput3)

#finding the smallest number:
if userInput1 < userInput2 and userInput1 < userInput3:
    print(userInput1)
elif userInput2 < userInput1 and userInput2 < userInput3:
    print(userInput2)
elif userInput3 < userInput1 and userInput3 < userInput2:
    print(userInput3)
    
