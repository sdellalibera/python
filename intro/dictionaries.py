from typing import List,Dict

dict = {}
dict["Alice"] = 25
print(type(dict))

def create_dictionary(name: str, age: int) -> Dict[str,int]:
    return {name:age}

dict1 = create_dictionary("alice",25)

names = ["Marco","Mario","Matteo"]

def list_to_dict(words: List[str]) -> Dict[str,int]:
    dictionary = {}
    for i in range(len(words)):
        w = words[i]
        dictionary[w] = i
    return dictionary

print(list_to_dict(names))

# it over writes the key value
my_dict = {"a": 1}
my_dict["a"] = 4
print(my_dict["a"])