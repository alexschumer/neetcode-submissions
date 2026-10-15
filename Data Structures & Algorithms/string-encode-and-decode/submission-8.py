class Solution:
    # we are combining a list of strings into a single string and then decoding that string after simulating being sent over a network.
    def encode(self, strs: List[str]) -> str:
        # for each string get the number of characters in the string.
        # append the length + '#' + plus the word to a new string to be exported.
        res = ""
        parts = []
        for word in strs:
            parts.append(str(len(word)))
            parts.append("#")
            parts.append(word)
        res = "".join(parts)
        return res
    def decode(self, s: str) -> List[str]:
    # we know the two characters of the string will be a int and #. 
    # we will get the size of the first word and slice to get the word.
    # we will jump to the next number (becuase we know where the last word ended) of the next word and repeat.
        res = []
        # i am going to use two pointer method to iterator and manipulate the string. I feel I have more control that way.
        i = 0
       
        while i < len(s):
            j = i
            while j < len(s) and s[j] != '#':
                j += 1
            length = int(s[i:j])
            word = s[j+1 : j+length+1]
            res.append(word)
            i = j + length + 1
        
        return res
