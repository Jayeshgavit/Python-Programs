from rich import print

print("\n")
print("[bold magenta]STATEMENT: Write a program to open three files 1.txt, 2.txt, and 3.txt. If any of these files are not present, a message without exiting the program must be printed prompting the same.[/bold magenta]".center(50, '-'))
print("\n")


try:
    with open('file.txt') as f:
        fr1 = f.read()
        print("File 1 Content:", fr1)

except Exception as e:
    print(f"File not found... check again!! {e}")

try:
    with open('test1.txt') as f:
        fr1 = f.read()
        print("File 1 Content:", fr1)

except Exception as e:
    print(f"File not found... check again!! {e}")

finally:
    print("Program finished")





'''
try:
    with open('file.txt') as f, open('test.txt') as f2, open('txt.txt') as f3:
        fr1 = f.read()
        fr2 = f2.read()
        fr3 = f3.read()
        print("File 1 Content:", fr1)
        print("File 2 Content:", fr2)
        print("File 3 Content:", fr3)

except FileNotFoundError:
    print("File not found... check again!!")

finally:
    print("Program finished")
    
'''