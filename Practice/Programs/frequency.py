def frequency_of_word(strings):
    words = strings.split()
    dict = {}
    for word in words:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1

    return dict

print(frequency_of_word("dd hggbj hgg fffh fff"));