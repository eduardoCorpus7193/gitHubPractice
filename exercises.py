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