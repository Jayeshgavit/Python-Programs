

price: float = 1234.2233434
print("Price : ", round(price,2))

# Using f-string
print(f"Price (.2f): {price:.2f}")
#increase readability
print(f"Price (.2f): {price:,.2f}")


#Increase Number Readability
number: int = 1000000
print(f"Number: {number:_}")
print(f"Number: {number:,}")

#dealing with date and time

from datetime import datetime 

now: datetime = datetime.now()
print(f"Now: {now:%d-%m-%y (%H:%M:%S)}")
print(f"Now: {now:%c}")
print(f"Now: {now:%I%p}")