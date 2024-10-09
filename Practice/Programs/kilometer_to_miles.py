# Python Program to convert kilometers to miles 
'''
1 km = 0.621371
'''
text = "Converting kilometer to miles"
print(text.center(50, "-"))

def km_to_miles(km):
            km_rs = km * 0.621371
            print(f"{km} km to {km_rs:.2f} miles".center(50, ":"))

while True:
    try:
        km = float(input("Enter km (0 for exiting) : "))
        if km == 0:
            break;
        km_to_miles(km)
    except ValueError:
          print("Invalid input. Please enter a numeric value.")
          
          





