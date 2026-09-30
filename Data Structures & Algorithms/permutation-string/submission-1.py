class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # sliding window of fixed size len(s1)
        # start the window off at an index at a character in s1

        s1_map = [0] * 26
        for ch in s1:
            s1_map[ord(ch) - ord('a')] += 1
        
        l = 0
        while l < len(s2) and s1_map[ord(s2[l]) - ord('a')] < 1:
            l += 1
        r = l + len(s1) - 1

        while r < len(s2):
            seen_map = [0] * 26
            for i in range(l, r + 1):
                seen_map[ord(s2[i]) - ord('a')] += 1
            if seen_map == s1_map:
                return True
            else:
                l += 1
                while l < len(s2) and s1_map[ord(s2[l]) - ord('a')] < 1:
                    l += 1
            r = l + len(s1) - 1
        return False
                
        

