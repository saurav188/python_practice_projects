def shortest_unique_prefix(words):
    output=[]
    for word1 in words:
        temp=0
        for word2 in words:
            if word1==word2:
                continue
            for i in range(len(word1)-1,-1,-1):
                if i>(len(word2)-1):
                    continue
                if word1[:i]==word2[:i]:
                    if i+1>temp:
                        temp=i+1
                        break
        output.append(word1[:temp])
    return output

print(shortest_unique_prefix(['joma', 'john', 'jack', 'techlead']))
# ['jom', 'joh', 'ja', 't']