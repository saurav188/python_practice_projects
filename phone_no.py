lettersMaps = {
    1: [],
    2: ['a', 'b', 'c'],
    3: ['d', 'e', 'f'],
    4: ['g', 'h', 'i'],
    5: ['j', 'k', 'l'],
    6: ['m', 'n', 'o'],
    7: ['p', 'q', 'r', 's'],
    8: ['t', 'u', 'v'],
    9: ['w', 'x', 'y', 'z'],
    0: []
}

validWords = ['dog', 'fish', 'cat', 'fog']

def makeWords(phone):
    def helper(phone,index,current_word):
        if index>=len(phone):
            return [current_word]
        output=[]
        number=int(phone[index])
        letters=lettersMaps[number]
        for letter in letters:
            for word in validWords:
                if current_word+letter==word[:index+1]:
                    output+=helper(phone,index+1,current_word+letter)
        return output
    temp=helper(phone,0,"")
    dict={}
    for i in range(len(temp)):
        if dict.get(temp[i])==None:
            dict[temp[i]]=True
        else:
            temp.pop(i)
    return temp

print(makeWords('364'))
# ['dog', 'fog']