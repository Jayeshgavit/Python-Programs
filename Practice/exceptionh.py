a,b = 10, 0
try:
    rs = a / b ;

except ValueError:
    print("Invalid input! Please enter a number.")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except:
    print("An unknown error occurred: ")

else:
    print("The result is ", rs)

finally:
    print("Program finished")   




'''

try block: Code that might raise an exception is placed in the try block.
except block: This block is executed if an exception occurs in the try block. You can specify the type of exception you want to catch (e.g., ValueError, IOError).
else block: Executed if no exception occurs in the try block.
finally block: Code inside this block will run no matter what, even if an exception occurs. It’s usually used for cleanup actions like closing files.

'''