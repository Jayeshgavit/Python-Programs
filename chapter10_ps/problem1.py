


f = open("text.txt")
content = f.read()

if ('twinkle' in content):
    print("presnt in content")
else: 
    print("Not present in content")




# with open("text.txt") as f:
#     content1 = f.read()
#     if "twinkle" in content1:
#         print("File exists and its content is 'twinkle'")
#     else:
#         print("File does not exist or its content is not 'twinkle'")