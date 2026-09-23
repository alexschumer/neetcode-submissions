class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # it does not seem like we are concerned with duplicates.
        # we do need to think about looping to the begining of the array from the end.
        # problem: multiply all the elements in the nums list not including selft (ith) index.
        # i dont think hashmap or set will help us here. we can use two pointers to navigate the window easily.
        left = [1] * len(nums)
        right = [1] * len(nums)
        res = [1] * len(nums)

        for i in range(len(nums)):
            if i == 0: continue
            left[i] = left[i - 1] * nums[i - 1]
        for i in range(len(nums)-2, -1, -1):
            if i == len(nums): continue
            right[i] = right[i+1] * nums[i+1]
        for i in range(len(nums)):
            res[i] = left[i] * right[i]
        return res