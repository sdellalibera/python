from typing import List,Set

numbers = [1,2,3,4,5]
numbers1 = [1,2,3,4,4]

def has_duplicates(numbers:List[int]) -> bool:
# create set directly
    return len(set(numbers)) != len(numbers)

print(has_duplicates(numbers))
print(has_duplicates(numbers1))
