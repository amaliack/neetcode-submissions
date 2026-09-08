class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # use 26-length array for each word and create a tuple and
        # add to hash map the words
        hash = {}
        for word in strs:
            char_arr = [0] * 26
            for letter in word:
                char_arr[ord(letter) - ord('a')] += 1
            tuple_version = tuple(char_arr)
            if tuple_version in hash:
                hash[tuple_version].append(word)
            else:
                hash[tuple_version] = [word]
        
        final = []
        for key, value in hash.items():
            final.append(value)
        return final
        
