x,y = 3,5
print(x == y)
print(x != y)
print(x < y)
print(x > y)

def check_balance(balance:int) -> None:
    if balance < 100:
        print('Balance too low')

check_balance(99)

# if scope doesnt give a shit basically 
# you can access variables inside an if scope
if(True):
    n = 10
print(n)
