class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded += chr(len(string))
            encoded += string
        return encoded

    def decode(self, s: str) -> List[str]:
        output = []
        i=0
        while i < len(s):
            length = ord(s[i])
            word = s[i+1:i+length+1]
            output.append(word)
            i += (length+1)
        return output