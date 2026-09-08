class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = "!"
        for string in strs:
            encoded += str(len(string)) + "!" + string + "!"
        print(encoded)
        return encoded[:-1]

    def decode(self, s: str) -> List[str]:
        decoded = []
        count = 1
        while count < len(s):
            length = ""
            while s[count] != "!":
                length += s[count]
                count += 1
            length = int(length)

            new_string = ""
            count += 1
            for i in range(length):
                new_string += s[count]
                count += 1
            count += 1
            decoded.append(new_string)
            print(new_string)
        return decoded