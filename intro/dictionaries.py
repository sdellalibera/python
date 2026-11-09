names = ["Marco","Mario","Matteo"]

def create_dictionary(name: str, age: int) -> dict[str,int]:
    return {name:age}

def list_to_dict(words: list[str]) -> dict[str,int]:
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