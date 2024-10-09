# Python Program to convert kilometers to miles 
'''
1 km = 0.621371
'''
text = "Converting kilometer to miles"
print(text.center(50, "-"))
km = float(input(" Enter the km for conversion : "))


def km_to_miles(km):
    return km * 0.621371

miles = km_to_miles(km);
print(f"{km} km to {miles:.2f} miles".center(50, ":"))