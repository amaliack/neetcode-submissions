class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # use 26-length array for each word and create a tuple and
        # add to hash map the words
        hash = defaultdict(list)
        for word in strs:
            char_arr = [0] * 26
            for letter in word:
                char_arr[ord(letter) - ord('a')] += 1
            hash[tuple(char_arr)].append(word)
        return list(hash.values())
        
