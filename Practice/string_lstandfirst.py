def find_letters(S):

    words = S.split()
    print(words)
    first_letter = words[0][0].upper()
    last_letter = words[1][-1].upper()
    
    return f"{first_letter}.{last_letter}"

S = "Sam Harris"
result = find_letters(S)
print(result) 
