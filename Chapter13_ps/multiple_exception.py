
print(" Program which represent multiple exception concept ".center(80, '-'))
print("\n")


try:
    result = 10 / 2
    print("Result : ", result)

    with open('file2.txt', 'r') as f:
        data = f.read()
        print("File data : ", data)

except (ValueError, ZeroDivisionError, TypeError, FileNotFoundError) as e:
    print("An error occurred: ", e)
