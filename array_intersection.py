class Solution:
    def intersection(self, nums1, nums2):
        nums1.sort()#O(nlogn)
        nums2.sort()#O(mlogm)
        intersection=[]
        i=0
        j=0
        while i<len(nums1) and j<len(nums2):#O(min(n,m))
            if nums1[i]==nums2[j]:
                intersection.append(nums1[i])
                i+=1
                j+=1
            elif nums1[i]>nums2[j]:
                j+=1
            else:
                i+=1
        return intersection

print(Solution().intersection([1,2,2,1],[2,2]))