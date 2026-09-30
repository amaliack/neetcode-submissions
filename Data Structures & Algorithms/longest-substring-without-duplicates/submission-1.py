class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # we can keep a hash/26-length array that stores frequencies
        # on window movement, we increment based on letter arriving/leaving window
        if not s:
            return 0

        hash_set = defaultdict(int)
        l = 0
        r = 1
        hash_set[s[l]] += 1
        max_len = 1
        while r < len(s):
            hash_set[s[r]] += 1
            while l < len(s) and hash_set[s[r]] > 1:
                hash_set[s[l]] -= 1
                l += 1
                continue
            max_len = max(max_len, r - l + 1)
            r += 1
        return max_len

