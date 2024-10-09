
# Python Program to Check leap Year or not
def leap_year(year):
    if year % 4 == 0:
        return f"{year} is leap year." 
    elif year % 100 ==0 and  year % 400 == 0:
        return f"{year} is leap year."
    else:
        return f"{year} is not a leap year."
    
year = int(input(" Enter Year : "))
print(leap_year(year))
