# VARIABLES TYPE
print(type([1,2,3]))
variable = 10
print(type(variable))
variable = "Hello"
print(type(variable))
variable = [1,2,3]
print(type(variable))

int = 10 # integer
floating = 98.5 # floating-point number
boolean = True # boolean
string = "hello" # string
string1, string2 = "hello", "everybody" #declare multiple variables in a single line
set = {1,2,4,5,7,7} # set (dont have duplicates)
list = [1,2,3,4,5] # list
tuple = (1,2) # tuple
tuple2 = (1,2,3) # tuple
dict = {string:"key",string:"value"} # dictionary

# print 
print(int)
print(string)
print(string1,string2)

string1, string2 = string2, string1 # swapping value without tmp variable

print(string1,string2)
print(set)
print(list)
print(tuple)
print(tuple2)
print()

# TYPE ERRORS
# message = "Hello" the casting wont work
message = "10"
message = int(message)
print(message)

# CASTING

pi = 3.14
square_root_8 = 2.82

pi = int(pi)
square_root_8 = int(square_root_8)

print(pi)
print(square_root_8)

var = None # absense of value