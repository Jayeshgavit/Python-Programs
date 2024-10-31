
number: int = 25

price: float = 23.34

name: str = "John Doe"

is_student: bool = False

passengers: list[str] = ['bob', 'hhg'] 
ages: list[str] = ["12", "23", "34", "45", "456"]

def evens_find(ages: list[str]) -> list[int]:
    even_ages = []
    for age in ages:
        try:
            age_int = int(age)
            if age_int % 2 == 0:
                even_ages.append(age_int)
        except ValueError:
            print(f"Invalid age: {age}")
    return even_ages

even_ages = evens_find(ages)
print(even_ages)
