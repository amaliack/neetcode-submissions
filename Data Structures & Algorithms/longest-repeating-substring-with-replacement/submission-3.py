class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window, where we adjust size based on the number of elements not the same
        # as the first letter in the window

        # so for AAABABB we start at AA --> AAA --> AAAB. This requires one replacement to get
        # four A's in a row, which we are allowed: AAABA --> AAABAB. Since we have two B's now,
        # we need two replacements to get this to work

        # target letter is whatever the left is?
        # we move the right until > k replacements needed from [l, r] to have all target letter

        if len(s) == 1:
            return 1
        
        l = 0
        r = 1
        window_map = [0] * 26
        window_map[ord(s[l]) - ord('A')] += 1
        max_el = ord(s[l]) - ord('A')
        max_el_count = 1
        replacements = 0
        max_len = 1
        while r < len(s):
            char_index = ord(s[r]) - ord('A')
            window_map[char_index] += 1
            # we check which is the new maximum element
            if window_map[char_index] > max_el_count:
                max_el_count = window_map[char_index]
                max_el = char_index
            replacements = abs(max_el_count - (r - l + 1))
            if replacements <= k:
                max_len = max(max_len, r - l + 1)
            else:
                window_map[ord(s[l]) - ord('A')] -= 1
                if max_el == (ord(s[l]) - ord('A')):
                    max_el_count -= 1
                l += 1
            r += 1
        return max_len



