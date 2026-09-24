class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # looks like duplicates are not counted. which tells me to use a set.
        # sliding window might be good here so we can get a live view of the size, keeping track of each window size.
        # might be best to sort the list first... but sorting is O(1)
        # could still do a sliding window of sorts and find the elemnts that are one greater than the left pointer while incrementing the right pointer. but the list isn't sorted... nevermind.
        new_nums = set(nums)
        print(new_nums)
        longest = 0
        for num in nums:
            if num - 1 not in new_nums:
                count = 1
                while num + count in new_nums:
                    count += 1
                longest = max(longest, count)

        return longest