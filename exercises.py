def operation(firstNumber, secondNumber, operand):				#function to calculate the selected operation
	if operand =="+":											#sum
		resultado = firstNumber + secondNumber					#sum operation
	elif operand == "-":										#substraction
		resultado = firstNumber - secondNumber					#substraction operation
	elif operand == "/":										#division
		resultado = firstNumber / secondNumber					#division operation
	elif operand == "*":										#multiplication
		resultado = firstNumber * secondNumber					#multiplication operation
	return resultado											#result return

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
myDictionary = { "Name":"Eduardo","Lastname":"Corpus","Age":26 }		#creating the dictionary with default data
print("Printing the data of the dictionary")		
print(myDictionary)			#printing the dictionary
myDictionary["Name"] = input(print("Write your name: "))		#saving the name on the dictionary
myDictionary["Lastname"] = input(print("Write your last name: "))		#saving the lastname on the dictionary
myDictionary["Age"] = input(print("Write your age: "))			#saving the age on the dictionary
print("Printing the new data of the dictionary")			
print(myDictionary)			#printing dictionary
sino = True		#declare boolean sino variable to use in the while loop
print("\nNow we will do a math operation")
while sino == True:			#starting while loop
	operand = input(print("Chose the operation you want to do(+,-,/,*)"))
	if operand == "+":			#validating if sum
		sino = False
		break			#exit the while loop
	elif operand == "-":			#validating if substraction
		sino == False
		break			#exit the while loop
	elif operand == "/":			#validating if division
		sino == False
		break			#exit the while loop
	elif operand == "*":			#validating if multiplication
		sino == False
		break			#exit the while loop
	else:
		print("Wrong answer") 		#if the user give a different answer restart the while loop
firstNumber = int(input(print("Write the first number"))) 		#declare and read the first number to the operation
secondNumber = int(input(print("Write the second number")))		#declare and read the second number to the operation
print("The operation result is: " + str(operation(firstNumber, secondNumber, operand))) 		#calling the function to do the operation and printing the result returned from the function