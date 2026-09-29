class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        1. input constraints --> alphanumeric, ignore non alphanumeric, length of 1
        2. empty input --> input has to be at least 1
        3. positive/negative --> doesn't matter
        4. duplicates --> not relevant
        5. modify input --> unlikely since the order of the input matters
        6. edge cases --> case-insensitive nad ignore non-alphanumeric

        brute force --> create a new string for "reading" the word backwards, check similarity
        invariant:
        - the bottleneck here is creating a new string, adding memory
        - we can solve this by bringing two pointers toward the middle (beg, end)
        """
        def isAlphaNumeric(c: str) -> bool:
            int_version = ord(c)
            if (int_version >= 48 and int_version <= 57 or 
                int_version >= 65 and int_version <= 90 or
                int_version >= 97 and int_version <= 122):
                return True
            return False
        
        left = 0
        right = len(s) - 1
        while left < right:
            while left < right and not isAlphaNumeric(s[left]):
                left += 1
            while right > left and not isAlphaNumeric(s[right]):
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True










