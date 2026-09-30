class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # sliding window of fixed size len(s1)
        # start the window off at an index at a character in s1

        if len(s1) > len(s2):
            return False
        
        s1_map = [0] * 26
        s2_map = [0] * 26
        for i in range(len(s1)):
            s1_map[ord(s1[i]) - ord('a')] += 1
            s2_map[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            if s1_map[i] == s2_map[i]: matches += 1
        
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            r_index = ord(s2[r]) - ord('a')
            if s2_map[r_index] == s1_map[r_index]:
                matches -= 1
                s2_map[r_index] += 1
            else:
                s2_map[r_index] += 1
                if s2_map[r_index] == s1_map[r_index]: matches += 1
            
            l_index = ord(s2[l]) - ord('a')
            l += 1
            if s2_map[l_index] == s1_map[l_index]:
                matches -= 1
                s2_map[l_index] -= 1
            else:
                s2_map[l_index] -= 1
                if s2_map[l_index] == s1_map[l_index]: matches += 1

        return matches == 26
                
        

