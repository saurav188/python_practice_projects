def getletterposition(letter,order):
    for i in range(len(order)):
        if order[i]==letter:
            return i+1
    return 0
def isSorted(words, order):
    for word in words:
        for i in range(1,len(word)):
            letter_order=getletterposition(word[i-1],order)<=getletterposition(word[i],order)
            if not letter_order:
                return False
    not_in_order=True
    max_length=0
    for word in words:
        temp=len(word)
        if temp>max_length:
            max_length=temp
    for checking_letter_no in range(max_length):
        for i in range(1,len(words)):
            try:
                prev_letter_postion=getletterposition(words[i-1][checking_letter_no],order)
            except:
                prev_letter_postion=0  
            try:
                this_letter_postion=getletterposition(words[i][checking_letter_no],order)
            except:
                this_letter_postion=0  
            not_in_order=prev_letter_postion>this_letter_postion
            if not_in_order:
                return False
    return True
print(isSorted(["fghi", "efgh"], "zyxwvutsrqponmlkjihgfedcba"))
# False
print(isSorted(["zyx", "zyxw", "zyxwv"],
               "zyxwvutsrqponmlkjihgfedcba"))
# True

#Given a list of words, and an arbitrary alphabetical order, 
#verify that the words are in order of the alphabetical order.

#Example:
#Input:
#words = ["abcd", "efgh"], order="zyxwvutsrqponmlkjihgfedcba"

#Output: False
#Explanation: 'e' comes before 'a' so 'efgh' should come before 'abcd'

#Example 2:
#Input:
#words = ["zyx", "zyxw", "zyxwy"],
#order="zyxwvutsrqponmlkjihgfedcba"

#Output: True
#Explanation: The words are in increasing alphabetical order