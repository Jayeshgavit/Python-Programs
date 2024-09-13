try:

    file = open("test.txt", "r");
    filer = file.read();
    print(filer)
    
except FileNotFoundError:
    print("File not found")
