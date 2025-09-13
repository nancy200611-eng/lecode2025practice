#26.Remove duplicates from sorted array
class Solution(object):
    def removeDuplicates(self, nums):
        j = 1 #pointer for unique  position
        for i in range(1,len(nums)):  #start from 2nd element
            if nums[i] != nums[i-1]:  #found a unique number
                nums[j] = nums[i]     #place in unique zone
                j+=1
        return j
            
        
