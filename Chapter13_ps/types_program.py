from typing import List, Tuple, Dict, Union

# List of integers
num: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]

# Tuple of strings
person: Tuple[str, str, str] = ('jay', 'navi', 'test')

# Dictionary with string keys and integer values
age_dict: Dict[str, int] = {'jay': 25, 'navi': 30, 'test': 40}

# Union of int or str
data: Union[int, str] = 42  # You can also assign a string value here, e.g., "Hello"

print(num)
print(person)
print(age_dict)
print(data)

