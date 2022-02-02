#Name: Raymond J. Spieldenner
#Assignment: If Else - Project: Sorting Numbers
#Date: 02/02/2022

#Input Variables:

userInput1 = int(input('Please input first number: '))
userInput2 = int(input('Please input second number: '))
userInput3 = int(input('Please input third number: '))

#Sorting Variables:

smallest = 0
middle = 0
largest = 0

#Finding the largest number:
if userInput1 > userInput2 and userInput1 > userInput3:
    largest = userInput1
elif userInput2 > userInput1 and userInput2 > userInput3:
    largest = userInput2
elif userInput3 > userInput1 and userInput3 > userInput2:
    largest = userInput3

#Finding the middle number:
#if input one is more than the second but less then the third
if userInput1 > userInput2 and userInput1 < userInput3:
    middle = userInput1
    #if 2 is more than 1 but less then 3
elif userInput2 > userInput1 and userInput2 < userInput3:
    middle = userInput2
    #if 3 is more than 1 but less than 2
elif userInput3 > userInput1 and userInput3 < userInput2:
    middle = userInput3

#finding the smallest number:
    #1 is bottom
if userInput1 < userInput2 and userInput1 < userInput3:
    smallest = userInput1
    #2 is bottom
elif userInput2 < userInput1 and userInput2 < userInput3:
    smallest = userInput2
    #3 is the bottom
elif userInput3 < userInput1 and userInput3 < userInput2:
    smallest = userInput3

#This final block is to re-examine the third input so that if it's the lesser value, it still prints. That was
#an issue I was having, where the median number wouldn't print if userInput3 was less than both of the other inputs.
if userInput3 < userInput2 and userInput3 < userInput1:
    smallest = userInput3
if userInput2 < userInput1:
    largest = userInput1
    middle = userInput2
else:
    largest = userInput2
    middle = userInput1
#Print statements:

print(smallest, "is the lesser value")
print(middle, "is the median value")
print(largest, "is the greater value")
