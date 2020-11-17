def chainedWords(words):
    first_letters={word[0]:True for word in words}
    last_letters={word[-1]:True for word in words}
    for key in first_letters:
        if last_letters.get(key)==None:
            return False
    for word in words:
        if word[-1] in first_letters and first_letters[word[-1]]:
            first_letters[word[-1]]=False
    for key in first_letters:
        if first_letters[key]:
            return False
    return True

print(chainedWords(['apple', 'eggs', 'snack', 'karat', 'tuna']))
#True