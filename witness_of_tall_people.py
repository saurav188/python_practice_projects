#There are n people lined up, and each have a height represented
#as an integer. A murder has happened right in front of them, and 
#only people who are taller than everyone in front of them are able 
#to see what has happened. How many witnesses are there?

def witnesses(heights):
    output=[heights[len(heights)-1]]
    for i in range(len(heights)-1,1,-1):
        if heights[i-1]>heights[i]:
            output.append(heights[i-1])
    return len(output)

print(witnesses([3, 6, 3, 4, 1]))