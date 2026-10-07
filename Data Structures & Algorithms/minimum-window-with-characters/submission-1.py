class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # think we can use a similar approach to earlier with the 26-length arrays (upper + lower!!)
        # we can do the matches thing from earlier, but the twist here is that window isn't fixed size
        # when do we change the size of the window? (has to be at least len(t))
        #   --> we could move the right until all characters in t are present
        #   --> from there, we move the left pointer until that's no longer the case
        #   --> we save this, and then move the left pointer until doing so impact # of matches
        #   --> we can repeat this process until the right pointer is all the way there

        if len(t) > len(s):
            return ""

        l = 0
        t_map = defaultdict(int)
        s_map = {}
        for i in range(len(t)):
            t_map[t[i]] += 1
            s_map[t[i]] = 0
        
        matches = 0
        min_len = len(s) + 1
        min_indices = (len(t), len(t))
        for r in range(len(s)):
            if s[r] in s_map:
                s_map[s[r]] += 1
                if s_map[s[r]] == t_map[s[r]]: matches += 1
            while matches >= len(t_map):
                if (r - l + 1) < min_len:
                    min_len = r - l + 1
                    min_indices = (l, r)
                if s[l] in s_map:
                    if s_map[s[l]] == t_map[s[l]]: matches -= 1
                    s_map[s[l]] -= 1
                l += 1
        return s[min_indices[0]: min_indices[1] + 1] if min_len <= len(s) else ""
        
