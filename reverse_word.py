def reverse_words(words):
    result=[]
    i=0
    for j in range(1,len(words)):
        if words[j]==" ":
            result=words[i:j]+[" "]+result
            i=j+1
    result=words[i:]+[" "]+result
    return result

s = list("can you read this")
s=reverse_words(s)
print(''.join(s))
# this read you can