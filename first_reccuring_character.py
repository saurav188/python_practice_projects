def first_recurring_char(s):
    dict={}
    for letter in s:
        if dict.get(letter)==None:
            dict[letter]=True
        else:
            return letter
    return None
  
print(first_recurring_char('qwertty'))
# t

print(first_recurring_char('qwerty'))
# None