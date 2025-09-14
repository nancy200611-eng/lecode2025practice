# 217 Contains Duplicate
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()             #Empty set

        for num in nums:         #loops through each number in list-nums
            if num in seen:      #cheks if the element exits in set-seen
                return True      #duplicates are present
            seen.add(num)        #add the element in the set-seen if not there
        else:
            return False         #no duplicates
