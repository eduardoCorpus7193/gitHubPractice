def operation(firstNumber, secondNumber, operand):
	if operand =="+":
		resultado = firstNumber + secondNumber
	elif operand == "-":
		resultado = firstNumber - secondNumber
	elif operand == "/":
		resultado = firstNumber / secondNumber
	elif operand == "*":
		resultado = firstNumber * secondNumber
	return resultado

myList = []		#declarate list
for i in range(5): 		#for to ask for te user to fill the list
	num = int(input("Write the number you want to save in the position " + str(i) + ": "))		#asking the user to fill the list
	myList.append(num)		#filling the list with the number given by the user
i = 0		#restart i variable to 0
for item in myList:		#for to print te list
    print("The number you write in the position " + str(i) + " is: " + str(item))		#printing the list
    i += 1 		#increment the i variable to print the postion of the list
myTuple = (0,1,2,3,4,5,6)		#declarating the tuple
length = len(myTuple)		#getting the tuple's length
i = 0		#restart i variable to 0
while i < length:		#loop while
    print("The number saved in the tuple in the " + str(i) + " position is: " + str(myTuple[i]))		#printing the tupla's data
    i += 1		#increment i variable
myDictionary = { "Name":"Eduardo","Lastname":"Corpus","Age":26 }
print("Printing the data of the dictionary")
print(myDictionary)
myDictionary["Name"] = input(print("Write your name: "))
myDictionary["Lastname"] = input(print("Write your last name: "))
myDictionary["Age"] = input(print("Write your age: "))
print("Printing the new data of the dictionary")
print(myDictionary)
sino = True
print("\nNow we will do a math operation")
while sino == True:
	operand = input(print("Chose the operation you want to do(+,-,/,*)"))
	if operand == "+":
		print("suma")
		sino = False
		break
	elif operand == "-":
		print("resta")
		sino == False
		break
	elif operand == "/":
		print("division")
		sino == False
		break
	elif operand == "*":
		print("multiplicacion")
		sino == False
		break
	else:
		print("Wrong answer")
firstNumber = int(input(print("Write the first number")))
secondNumber = int(input(print("Write the second number")))
print("The operation result is: " + str(operation(firstNumber, secondNumber, operand)))