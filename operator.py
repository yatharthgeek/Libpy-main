# Python Logical Operators

apple = int(input("How much apples you have ?"))

if apple == 21 :
	print(" You have 21 Apples")
	
elif apple == 23 :
	print("You have 23 apples")
	

# Now with the logical operators 

if apple == 21 or apple == 23 :
	print("There are "+str(apple) +" Apples ")
	
	# with use of logical operators we can actually make things easier 
	# the or operator is used with you have to make either of the two or more conditions correct 
	
	# if any condition inside it is found true then the print function is executed 
	
name = input("Enter Name : ")

if name == "Ram" or name == "Mohan" :
	print(name+" already exists in our database")

else :
	print("Welcome "+name)
	

	