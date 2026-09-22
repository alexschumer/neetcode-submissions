class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # k is the top k most frequent numbers in the list.
        # we will need to keep track of how many times a number occurs in the list.
        # it would be great if that list was ordered so we can just take the larget k number of elements in the hashmap.
        found = defaultdict(int)

        # for each num in nums, count how many occurances there are of each number.
        for num in nums:
            found[num] += 1
        res = sorted(found.items(), key=lambda pair: pair[1], reverse=True)
        return [pair[0] for pair in res[:k]]    