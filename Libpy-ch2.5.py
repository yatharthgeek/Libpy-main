# Data types

# 1.  The integer 

integer = 12 

# the integer data type is data type of numbers 
# Any number you see is mostly integer data type 

print(type(integer))

# the type() function is used to check which data type the following variable has 

# 2.  the Float 

float = 12.9 

# the decimal data types are always float 

print(type(float))

# 3. The Strings 

strings = "I am Groot"

# Anything inside " " are strings 

print(type(strings))

# A number when written in " " also becomes string 

string_num = "28"

print(type(string_num))


# If we try to concate different data types error occurs 

#cancate = integer+strings

#print(concate)

# To prevent this problem we use some conversion techniques 

# 1  . conversion of integers to strings 

convert_str = str(integer)

# the str() function is used to convert the following 

print(type(convert_str))

# 2 . conversion of Strings to integer 

convert_int = int(string_num)

# the int() function does the same 

print(type(convert_int))

