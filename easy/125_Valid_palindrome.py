class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        Str = ""                        # Step 1: Initialize an empty string to store filtered characters
        for char in s:                  # Step 2: Loop through each character in the input string
            if char.isalnum():          # Keep only alphanumeric characters (ignore spaces, symbols, etc.)
                Str += char.lower()     # Convert to lowercase and add to Str (case-insensitive comparison)

        return Str == Str[::-1          # Step 3: Compare the cleaned string with its reverse


        
