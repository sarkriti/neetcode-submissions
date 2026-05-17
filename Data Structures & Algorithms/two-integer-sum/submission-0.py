class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i,j in enumerate(nums):
            diff = target - j
            #is diff in our hashmap? the numbers are our values and the idx key
            if diff in hashmap:
                return [hashmap[diff],i]
            hashmap[j] = i

        