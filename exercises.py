my_list = []
for i in range(5):
	num = int(input("Write the number you want to save in the position " + str(i) + ": "))
	my_list.append(num)
i = 0
for item in my_list:
    print("The number you write in the position " + str(i) + " is: " + str(item))
    i += 1