
command = "start"

match command:
    case "start":
        print("Starting...")

    case "stop":
        print("Stopping...")

    case _:
        print("Invalid command. Please try again.")



person = {"name": "Jay", "age": 30}

match person:
    case {"name": name, "age": age}:
        print(f"Name: {name}, Age: {age}")
    case _:
        print("No match")


items = [1, 2]

match items:
    case [1, 2]:
        print("Matched the list [1, 2]")
    case [1, _]:
        print("Matched a list starting with 1")
    case _:
        print("No match")


value = 15

match value:
    case x if x < 10:
        print(f"{x} is less than 10")
    case x if x >= 10:
        print(f"{x} is greater than or equal to 10")

