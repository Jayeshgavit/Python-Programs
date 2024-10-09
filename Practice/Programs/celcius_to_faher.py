
# Python program to convert Celcius to Feharaheit


def conversion(celcius):
    return ((celcius * 9/5) + 32)

celcius = float(input("Enter temperature in Celcius: "))
fahrenheit = conversion(celcius)
print(f" temperature is {celcius} and fahrenheit is {fahrenheit}")