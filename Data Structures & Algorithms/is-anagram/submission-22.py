class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # returning a bool.
        # we need to keep track of the number of occurances for each letter in each string.
        if len(s) != len(t): return False

        found_s = defaultdict(int)
        found_t = defaultdict(int)

        for i in range(len(s)):
            found_s[s[i]] += 1
            found_t[t[i]] += 1

        return found_s == found_t