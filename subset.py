def get_subset_iterate(set):
    subsets=[[]]
    for i in range(len(set)):
        temp=[[]]*len(subsets)
        for j in range(len(subsets)):
            temp[j]=''.join(subsets[j])+set[i]
        subsets=subsets+temp
    return subsets

print(get_subset_iterate(['1','2','3','4']))

#[]
#[] [1] (this + function that gives (this+1)th items recurred len(set) times
#[] [1] [2] [1,2]
#[] [1] [2] [1,2] [3] [1,3] [2,3] [1,2,3]
def helper(set,subset,i):
    if i==len(set):
        return None
    temp=[[]]*len(subset)
    for j in range(len(temp)):
        temp[j]=''.join(subset[j])+set[i]
    subset=subset+temp
    i+=1
    next=helper(set,subset,i)
    if next!=None:
        return next
    return subset

def get_subset_recursive(set):
    subset=[[]]
    i=0
    return helper(set,subset,i)

print(get_subset_recursive(['1','2','3','4']))
