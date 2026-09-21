class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # for each string in the list of strings, we need to group words that have the same characters together in their own sub lists.
        found = defaultdict(list)
        # for each string we want to sort the letters of the string.
        for string in strs:
            new_string = "".join(sorted(string))
            # then determine if they are already in the output hashmap.
            # if they are, add the word to the list.
            # if not, add to list.
            found[new_string].append(string)
        
        # return found hashmap as List of Lists
        return list(found.values())