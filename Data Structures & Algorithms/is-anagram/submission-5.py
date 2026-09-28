class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        1. input --> two strings s/t all lowercase English letters
        2. empty input --> strings are both at least 1 character long
        3. duplicates --> possible if s and t are same word, return True
        4. positive/negative --> not applicable
        5. sorted input --> not applicable (words aren't sorted by char)
        6. modify input --> leaning no (not necessary anyway)
        7. edge case behavior --> if s and t are not the same length, false

        brute force --> not really sure, probably O(n^2) where we go through both

        invariant --> we hash to keep track of frequencies
        """
        if len(s) != len(t):
            return False

        map_s = defaultdict(int)
        map_t = defaultdict(int)

        for ch in s:
            map_s[ch] += 1
        for ch in t:
            map_t[ch] += 1
        for key, val in map_s.items():
            if val != map_t[key]:
                return False
        return True