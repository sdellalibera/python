# function
def sum1(a,b):
    print(a + b)

# type hints
def sum2(a: int, b:int) -> int:
    print(a + b)

# default arguments
# if first is optional then also second has to be optional
def sum3(a,b = 10):
    print(a + b)
a,b = 1,2

sum1(1,2)
sum2(1,2)
sum3(1,2) # this overloads the default parameter 
sum3(1) # this uses b with default parameters

# THIS IS NOT VALID
# def sum4(a = 10,b):
#    print(a + b)
