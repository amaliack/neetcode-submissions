class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # we can use length 26 arrays since we know lowercase letters
        if len(s) != len(t):
            return False
        
        s_dict = [0] * 26
        for letter in s:
            s_dict[ord(letter) - ord('a')] += 1
        t_dict = [0] * 26
        for letter in t:
            index = ord(letter) - ord('a')
            t_dict[ord(letter) - ord('a')] += 1
            if t_dict[index] > s_dict[index]:
                return False
        
        """for index in range(0, 26):
            if s_dict[index] != t_dict[index]:
                return False"""
        return True