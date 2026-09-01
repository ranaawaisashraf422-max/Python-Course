from typing import List, Tuple, Dict, Union

#List of Integers

numbers : list[int] = [1,2,3,4,5,6]

#Tuple of a string and a integer

person : Tuple[str,int] = ["Awais" , 446]

#Dictionary with string key and integer value

scores : Dict[str,int] = {"Awais" : 99,
                          "Abeeha" : 89}

# Union type for variable that can hold multiple types
identifiers : Union [int,str] = "12IDFE"
#Identifiers = 12346 # Also Valid

print(numbers)
print(person)
print(scores)
print(identifiers)