class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # we can use length 26 arrays since we know
        s_dict = [0] * 26
        for letter in s:
            s_dict[ord(letter) - ord('a')] += 1
        t_dict = [0] * 26
        for letter in t:
            t_dict[ord(letter) - ord('a')] += 1
        for index in range(0, 26):
            if s_dict[index] != t_dict[index]:
                return False
        return True