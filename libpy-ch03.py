# Using some conditions 

val_1 = 12 
val_2 = 23 

print (val_1 < val_2 )
# if conditon satisfies , True is retured either false like 

print (val_1 > val_2)

# We can also compare some of the conditons using equal to as (==) and not equal to as (!=)

print(val_1 == val_2)

print(val_1 != val_2)

# some conditions like greater than equal or less than equal to can also be used as 

print(val_1 >= val_2)

print(val_1 <= val_2)

# we can create some of the conditions that only run when a particular conditons is true as 

if val_1 < val_2 :
	print("This statement is true ...  ")
	
	# the if statement is used to make a conditon which only satisfies when a particular condition is true 
	
	# when the if statement doesnt seems correct then what types of tasks will performed is been specified by the else statement 
	
if val_1 > val_2 :
	print("The statement is very ture ....")
	
else :
	print("The statement is False .... ")
	
	# in this example the if condition was not satisfied , so the interpreter runs the else statement
	
	# we can also use else statement with some conditions by using elif statement 
	
if val_1 > val_2 :
	print("The statement is very ture ....")
	
elif val_1 <= val_2 : 
	print("The elif statement is true .... ")
	
	# in this case we are using else statement with some conditions 
	
	# we can use as many elif we want 
	
	# if any of the one statement is fulfilled , the rest will not be printed 


if val_1 > val_2 :
	print("The statement is very ture ....")
	
elif val_1 <= val_2 : 
	print("The elif statement is true and the checkup stops here  .... ")
	
elif val_1 < val_2 :
	print("This is true but not be printed ")
	
	
	# we can also use else with elif if none of the conditions are fulfilled 
	
	
if val_1 > val_2 :
	print("Not true ..........")
	
elif val_1 == val_2 : 
	print("Not ture ")
	
elif val_1 >= val_2 :
	print("This is not true  ")
	
	
else :
	print("None was true so else printed ")
