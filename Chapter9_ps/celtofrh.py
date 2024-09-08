print(" Celcius to fehernheite \n")
def conversion(celcius):
    return ((celcius * (9/5)) + 32)


celcius = float(input(" Enter temperature : "))
print(conversion(celcius))


print("\nfehernheite to  Celcius  \n")
def conversion_to_(f):
    return ((5 * (f-32)) / 9)


Fehrenheite = float(input(" Enter Fehrenheite : "))
print(conversion_to_(Fehrenheite))