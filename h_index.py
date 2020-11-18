#The h-index is a metric that attempts to measure the productivity 
#and citation impact of the publication of a scholar. The definition 
#of the h-index is if a scholar has at least h of their papers cited 
#h times.
def hIndex(publications):
    length=len(publications)
    for i in range(length,0,-1):
        if i in publications:
            j=i
            for publication in publications:
                if publication>=i:
                    j-=1
            if j==0:
                return i
    return 0

print(hIndex([5, 3, 3, 1, 0]))
# 3
#There are 3 publications with 3 or more citations, hence the h-index is 3.