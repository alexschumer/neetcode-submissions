class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # returning a bool.
        # we need to keep track of the number of occurances for each letter in each string.
        return Counter(s) == Counter(t)