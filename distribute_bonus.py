def getBonuses(performance):
    bonus=[1 for i in performance]
    for i in range(len(performance)):
        #first person
        if i==0:
            if performance[i]>performance[i+1]:
                bonus[i]+=1
        #last person
        elif i==len(performance)-1:
            if performance[i]>performance[i-1]:
                bonus[i]+=1
        else:
            if performance[i]>performance[i+1]:
                bonus[i]+=1
            if performance[i]>performance[i-1]:
                bonus[i]+=1
    return bonus

print(getBonuses([1, 2, 3, 2, 3, 5, 1]))
# [1, 2, 3, 1, 2, 3, 1]
#Input:  [1, 2, 3, 2, 3, 5, 1]
#Output: [1, 2, 3, 1, 2, 3, 1]