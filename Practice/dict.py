
translations = {'Thank you': 'Dhanywad', 'Run': 'Dudna', 'Sit': 'Baithna', 'Sing': 'Gana Gau'}

user_input = input("Enter string: ").title()

found = False

for key in translations:
    if key == user_input:
        print(translations[key])
        found = True
        break

if not found:
    print("Not found")

