def jumpToEnd(nums):
    best_cases={}
    def helper(nums,start_index):
        if len(nums)-1<=start_index:
            return 1
        elif best_cases.get(start_index)!=None:
            return best_cases[start_index]
        end_index=len(nums)-1
        max_jump=nums[start_index]
        best_case=end_index+1
        for i in range(1,max_jump+1):
            temp=helper(nums,start_index+i)
            if temp<best_case:
                best_case=temp
        print(nums[start_index:],best_case+1)
        best_cases[start_index]=best_case+1
        return best_case+1
    return helper(nums,0)-1
        

print(jumpToEnd([3, 2, 5, 1, 1, 9, 3, 4]))
# 2
#Starting at index 0, for an element n at index i, you are allowed to 
#jump at most n indexes ahead. Given a list of numbers, find the 
#minimum number of jumps to reach the end of the list.
