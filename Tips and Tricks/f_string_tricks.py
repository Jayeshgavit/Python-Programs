

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