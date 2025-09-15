class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):                        # if lengths are not equal then they can't be anagrams
            return False
        
        countS , countT = {} ,{}                    # dictionaries to store frequency of characters in  's' and 't' 

        for i in range(len(s)):                     # iterate through both strings simultaneously
            countS[s[i]] = 1 + countS.get(s[i],0)   # update frequency count for characters at 's'
            countT[t[i]] = 1 + countT.get(t[i],0)   #update frquency count for characters at 't'

        return countS == countT                     # if both dictionaries are equal then they are anagrams
